
"""
write data into vtr files
"""

from pathlib import Path
import h5py
import numpy as np

def WriteVTRs(numOfBlocks:int, dirVTR:Path, dirHDF:Path)->None:
  h5 = h5py.File(dirHDF, 'r')

  # demo: write one block, if success, add other blocks
  filePathVTR = dirVTR.joinpath("1.vtr")
  vtr = open(filePathVTR, 'wb')

  vtr.write(b'<?xml version="1.0"?>\n')
  vtr.write(b'<VTKFile type="RectilinearGrid" version="0.1" byte_order="LittleEndian">\n')
  vtr.write(b'  <RectilinearGrid WholeExtent="    2   27    2   52    2   12">\n')
  vtr.write(b'  <Piece Extent="    2   27    2   52    2   12">\n')
  vtr.write(b'    <CellData>\n')
  vtr.write(b'    </CellData>\n')
  vtr.write(b'    <PointData>\n')
  # now only write P field
  vtr.write(b'      <DataArray type="Float64" Name="P" NumberOfComponents="1" format="appended" offset="    0"/>\n')
  vtr.write(b'    </PointData>\n')

  # coordinates are necessary
  vtr.write(b'    <Coordinates>')
  vtr.write(b'      <DataArray type="Float64" Name="Xcenter" NumberOfComponents="1" format="appended" offset="    116692"/>\n')
  vtr.write(b'      <DataArray type="Float64" Name="Ycenter" NumberOfComponents="1" format="appended" offset="    116904"/>\n')
  vtr.write(b'      <DataArray type="Float64" Name="Zcenter" NumberOfComponents="1" format="appended" offset="    117316"/>\n')
  vtr.write(b'    </Coordinates>')
  vtr.write(b'  </Piece>\n')
  vtr.write(b'  </RectilinearGrid>\n')
  vtr.write(b'  <AppendedData encoding="raw">\n')

  # add '_' to denote the starting floats data
  vtr.write(b'_')

  fieldP = h5["C001"]["Block-00-P"][:]  # “[:]” 不可少
  #print(len(fieldP))
  #print(fieldP[1010])
  print(type(fieldP))

  numOfBytes = (len(fieldP) * 8)#; print(numOfBytes, type(numOfBytes))

  numOfBytes = np.int32(numOfBytes)
  #print(numOfBytes, type(numOfBytes))
  # write the byte offsets
  numOfBytes.tofile(vtr)
  #fieldP.tofile(vtr, dtype=np.int, count=1)

  # write float data
  fieldP.tofile(vtr)

  # write coords X
  coordsX = h5["C001"]["Block-00-X"][:]
  #print(coordsX)

  numOfBytes = np.int32(len(coordsX) * 8)
  numOfBytes.tofile(vtr)

  coordsX.tofile(vtr)

  # write coords Y
  coordsY = h5["C001"]["Block-00-Y"][:]
  numOfBytes = np.int32(len(coordsY) * 8)
  numOfBytes.tofile(vtr)

  coordsY.tofile(vtr)

  # write coords Z
  coordsZ = h5["C001"]["Block-00-Z"][:]
  numOfBytes = np.int32(len(coordsZ) * 8)
  numOfBytes.tofile(vtr)

  coordsZ.tofile(vtr)

  vtr.write(b'\n')
  vtr.write(b'  </AppendedData>\n')
  vtr.write(b'</VTKFile>')

  #print(list(h5.keys())[0])

  pass