# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class plc
###########################################################################

class plc ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"示波器数据FFT分析软件", pos = wx.DefaultPosition, size = wx.Size( 800,655 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 1, 1, 0, 0 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5.SetMinSize( wx.Size( 800,200 ) ) 
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"示波器CSV文件路径", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText15.Wrap( -1 )
		
		self.m_staticText15.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer5.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer5.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"FFT分析波形为：勾选通道乘以对应系数的和。默认（CH1,CH2,CH3通道为三相电压电流，分析其0至1秒共模波形。）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		
		bSizer5.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 1, 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		self.m_scrolledWindow2.SetMinSize( wx.Size( 240,-1 ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3.SetMinSize( wx.Size( 240,-1 ) ) 
		m_checkList3Choices = []
		self.m_checkList3 = wx.CheckListBox( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_checkList3Choices, 0 )
		self.m_checkList3.SetMinSize( wx.Size( 240,-1 ) )
		
		bSizer3.Add( self.m_checkList3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow2.SetSizer( bSizer3 )
		self.m_scrolledWindow2.Layout()
		bSizer3.Fit( self.m_scrolledWindow2 )
		fgSizer1.Add( self.m_scrolledWindow2, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"示波器型号", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer51.Add( self.m_comboBox1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"基波频率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		
		bSizer51.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"谐波分析范围（次）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		
		bSizer51.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"801", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer31 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"起始时间T0（秒）", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText11.Wrap( -1 )
		
		bSizer8.Add( self.m_staticText11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_T0 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_T0, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer31.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"结束时间Tend（秒）", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText111.Wrap( -1 )
		
		bSizer91.Add( self.m_staticText111, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_Tend = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.m_Tend, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer31.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer51.Add( gSizer31, 1, wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 0, 4, 0, 0 )
		
		gSizer4.SetMinSize( wx.Size( -1,200 ) ) 
		bSizer52 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"CH1系数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		
		bSizer52.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, u"0.3333", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer52.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		
		gSizer4.Add( bSizer52, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"CH2系数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		
		bSizer9.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, u"0.3333", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		
		gSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"CH3系数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		
		bSizer10.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, u"0.3333", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl12, 0, wx.ALL, 5 )
		
		
		gSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"CH4系数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		
		bSizer11.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, u"0.3333", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl13, 0, wx.ALL, 5 )
		
		
		gSizer4.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer51.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"采样频率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		bSizer51.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_dt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dt.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.m_dt.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer51.Add( self.m_dt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"数据长度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		
		bSizer51.Add( self.m_staticText4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_len = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_len.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.m_len.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer51.Add( self.m_len, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Button1 = wx.Button( self, wx.ID_ANY, u"FFT分析", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Button1.SetMinSize( wx.Size( -1,40 ) )
		
		bSizer51.Add( self.Button1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"说明信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"版本信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu5, u"说明" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChanged )
		self.m_filePicker1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.m_checkList3.Bind( wx.EVT_LISTBOX, self.Box )
		self.m_checkList3.Bind( wx.EVT_LISTBOX_DCLICK, self.BoxDClick )
		self.m_checkList3.Bind( wx.EVT_CHECKLISTBOX, self.BoxToggled )
		self.Button1.Bind( wx.EVT_BUTTON, self.OnButtonClick )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection2, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection1, id = self.m_menuItem3.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFileChanged( self, event ):
		event.Skip()
	
	def SetFocus( self, event ):
		event.Skip()
	
	def Box( self, event ):
		event.Skip()
	
	def BoxDClick( self, event ):
		event.Skip()
	
	def BoxToggled( self, event ):
		event.Skip()
	
	def OnButtonClick( self, event ):
		event.Skip()
	
	def mOnMenuSelection2( self, event ):
		event.Skip()
	
	def mOnMenuSelection1( self, event ):
		event.Skip()
	

