import json
from subprocess import Popen, PIPE
from typing import Union
from functools import reduce
from htscf.db.mongo import connect
from uuid import uuid4
from pathlib import Path
from sys import platform
from uuid import uuid4
from htscf.utils.tools import writeScript


def workflow(rootPath: Union[Path, str], stepIds: list[str], dbName, stepsCollectionName, stepLogCollectionName, settingsCollectionName, host, port):
    """
    流程化计算
    按照【stepIds】中的顺序在【rootPath】中运行【dbName】数据库【stepsCollectionName】中的每个step
    :param rootPath: 流程运行根目录
    :param stepsCollectionName: 具体存储流程的collection
    :param settingsCollectionName: 每一步的临时配置数据的collection
    :param stepLogCollectionName: 每个流程记录的数据
    :param host: 数据库IP
    :param port: 数据库端口
    :param dbName: 数据库名
    :param stepIds: 按照顺序执行的过程ID
    """
    stepsCollection = connect(dbName, stepsCollectionName, host, port)
    stepLogCollection = connect(dbName, stepLogCollectionName, host, port)
    settingsCollection = connect(dbName, settingsCollectionName, host, port)
    rootPath = Path(rootPath)
    rootPath.mkdir(exist_ok=True, parents=True)
    stepInfo = list(map(lambda i: dict(_id=i), stepIds))

    def runStep(prevStepInfo: Union[dict, str], currentStepInfo: dict) -> dict:
        args = runBefore(rootPath, stepsCollection, settingsCollection, currentStepInfo, prevStepInfo)
        popen = Popen(args, stdout=PIPE)
        popen.wait()
        return runAfter(popen, currentStepInfo, stepLogCollection)

    reduce(runStep, stepInfo, "-1")


def runBefore(rootPath, stepsCollection, settingsCollection, currentStepInfo, prevStepInfo):
    """
    运行前的准备
    :param rootPath: 运行的根目录
    :param settingsCollection:
    :param stepsCollection:
    :param currentStepInfo:
    :param prevStepInfo:
    :return:
    """
    # 查询当前步骤的数据
    data = stepsCollection.find_one({
        "_id": currentStepInfo["_id"]
    })
    # 获取当前步骤的每个数据
    program = data["program"]  # 运行的程序名
    settings = data["settings"]  # 运行时传递的配置文件
    if prevStepInfo == "-1":
        prevLogId = "-1"
    else:
        prevLogId = prevStepInfo["logId"]  # 上一步运行输出的内容

    scriptText = data["script"]  # 运行的脚本内容
    scriptPath = writeScript(rootPath, scriptText)

    settingsId = f"settings-{uuid4()}"  # 生成随机配置id
    settingsCollection.insert_one({
        "_id": settingsId,
        "data": settings
    })
    flowId = uuid4().__str__()
    return [program, scriptPath, rootPath, settingsId, prevLogId, flowId]


def runAfter(popen, currentStepInfo, stepLogCollection):
    out = popen.stdout.read()
    try:
        if platform == "win32":
            outData = out.decode("gbk")
        else:
            outData = out.decode("utf-8")
    except Exception as e:
        print(f"在window平台解析错误:\n{e},\n切换为utf-8")
        outData = out.decode("utf-8")
    logId = f"{currentStepInfo['_id']}-{uuid4()}"
    stepLogCollection.insert_one({
        "_id": logId,
        "data": outData
    })
    return {
        "_id": currentStepInfo["_id"],
        "logId": logId
    }
