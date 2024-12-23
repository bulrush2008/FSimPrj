
"""
Train all fields by FNN model

@author     @data       @aff        @version
Xia, S      24.12.23    Simpop.cn   v3.x
"""

# -----------------------------------------------------------------------------
import torch

from pathlib import Path

from Common.Regression  import Regression
from Common.FSimDataset import FSimDataset

# -----------------------------------------------------------------------------
def train(numOfEpochs:int=5, fields:list=["T"], trainSet:list=["C001"], testSet:list=["C002"] )->bool:
  """
  Train the FNN model by a give trainset, in which some cases field included.
  """
  iSuccess = False

  #----------------------------------------------------------------------------
  # init of class of database
  filePathH5 = Path("../FSCases/FSHDF/MatrixData.h5")
  #aLive = filePathH5.exists()
  #print(aLive)

  #----------------------------------------------------------------------------
  # train fields

  ifield = 0

  for var in fields:
    ifield += 1
    fsDataset_train = FSimDataset(filePathH5, trainSet, var)

    # gen a obj as regression, and then train the model
    R = Regression(var)

    print(f"Now we train the {var} field:")

    # train the model
    epochs = numOfEpochs
    for i in range(epochs):
      print(f"  - Training Epoch {i+1} of {epochs} for {var}")
      for inp, label, _ in fsDataset_train:
        R.train(inp, label)
        pass
      pass

    # draw the history of lss
    DirPNG = Path("./Pics")
    R.saveLossHistory2PNG(DirPNG)
    pass

    # 预测，并与测试集比较
    # predict and compare with the test set
    fsDataset_test = FSimDataset(filePathH5, testSet, var)

    # for CXXX
    inp, _, coords = fsDataset_test[0]

    # 1-predict first and then write the predicting data to h5 database
    # coordinates are optional

    if ifield == 1:
      R.write2HDF(inp, Path("./fnn.h5"), coords=coords)
    else:
      R.write2HDF(inp, Path("./fnn.h5"), coords=None)

  iSuccess = True
  return iSuccess