///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jul 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

plc::plc( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxGridSizer* gSizer3;
	gSizer3 = new wxGridSizer( 1, 1, 0, 0 );
	
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	bSizer5->SetMinSize( wxSize( 800,200 ) ); 
	m_staticText15 = new wxStaticText( this, wxID_ANY, wxT("示波器CSV文件路径"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText15->Wrap( -1 );
	m_staticText15->SetFont( wxFont( 18, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("宋体") ) );
	
	bSizer5->Add( m_staticText15, 0, wxALL|wxEXPAND, 5 );
	
	m_filePicker1 = new wxFilePickerCtrl( this, wxID_ANY, wxEmptyString, wxT("Select a file"), wxT("*.*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	bSizer5->Add( m_filePicker1, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText10 = new wxStaticText( this, wxID_ANY, wxT("FFT分析波形为：勾选通道乘以对应系数的和。默认（CH1,CH2,CH3通道为三相电压电流，分析其0至1秒共模波形。）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText10->Wrap( -1 );
	bSizer5->Add( m_staticText10, 0, wxALL|wxEXPAND, 5 );
	
	wxFlexGridSizer* fgSizer1;
	fgSizer1 = new wxFlexGridSizer( 0, 2, 1, 1 );
	fgSizer1->SetFlexibleDirection( wxBOTH );
	fgSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_scrolledWindow2 = new wxScrolledWindow( this, wxID_ANY, wxDefaultPosition, wxSize( -1,-1 ), wxHSCROLL|wxVSCROLL );
	m_scrolledWindow2->SetScrollRate( 5, 5 );
	m_scrolledWindow2->SetMinSize( wxSize( 240,-1 ) );
	
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxVERTICAL );
	
	bSizer3->SetMinSize( wxSize( 240,-1 ) ); 
	wxArrayString m_checkList3Choices;
	m_checkList3 = new wxCheckListBox( m_scrolledWindow2, wxID_ANY, wxDefaultPosition, wxSize( -1,-1 ), m_checkList3Choices, 0 );
	m_checkList3->SetMinSize( wxSize( 240,-1 ) );
	
	bSizer3->Add( m_checkList3, 1, wxALL|wxEXPAND, 5 );
	
	
	m_scrolledWindow2->SetSizer( bSizer3 );
	m_scrolledWindow2->Layout();
	bSizer3->Fit( m_scrolledWindow2 );
	fgSizer1->Add( m_scrolledWindow2, 1, wxALL|wxEXPAND, 5 );
	
	wxBoxSizer* bSizer51;
	bSizer51 = new wxBoxSizer( wxVERTICAL );
	
	m_comboBox1 = new wxComboBox( this, wxID_ANY, wxT("示波器型号"), wxDefaultPosition, wxDefaultSize, 0, NULL, 0 ); 
	bSizer51->Add( m_comboBox1, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("基波频率"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer51->Add( m_staticText1, 0, wxALL|wxEXPAND, 5 );
	
	m_textCtrl1 = new wxTextCtrl( this, wxID_ANY, wxT("50"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer51->Add( m_textCtrl1, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText2 = new wxStaticText( this, wxID_ANY, wxT("谐波分析范围（次）"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2->Wrap( -1 );
	bSizer51->Add( m_staticText2, 0, wxALL|wxEXPAND, 5 );
	
	m_textCtrl2 = new wxTextCtrl( this, wxID_ANY, wxT("401"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer51->Add( m_textCtrl2, 0, wxALL|wxEXPAND, 5 );
	
	wxGridSizer* gSizer31;
	gSizer31 = new wxGridSizer( 0, 2, 0, 0 );
	
	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText11 = new wxStaticText( this, wxID_ANY, wxT("起始时间T0（秒）"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText11->Wrap( -1 );
	bSizer8->Add( m_staticText11, 0, wxALL|wxEXPAND, 5 );
	
	m_T0 = new wxTextCtrl( this, wxID_ANY, wxT("0"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer8->Add( m_T0, 0, wxALL|wxEXPAND, 5 );
	
	
	gSizer31->Add( bSizer8, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer91;
	bSizer91 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText111 = new wxStaticText( this, wxID_ANY, wxT("结束时间Tend（秒）"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText111->Wrap( -1 );
	bSizer91->Add( m_staticText111, 0, wxALL|wxEXPAND, 5 );
	
	m_Tend = new wxTextCtrl( this, wxID_ANY, wxT("1"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer91->Add( m_Tend, 0, wxALL|wxEXPAND, 5 );
	
	
	gSizer31->Add( bSizer91, 1, wxEXPAND, 5 );
	
	
	bSizer51->Add( gSizer31, 1, wxEXPAND, 5 );
	
	wxGridSizer* gSizer4;
	gSizer4 = new wxGridSizer( 0, 4, 0, 0 );
	
	gSizer4->SetMinSize( wxSize( -1,200 ) ); 
	wxBoxSizer* bSizer52;
	bSizer52 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText19 = new wxStaticText( this, wxID_ANY, wxT("CH1系数"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText19->Wrap( -1 );
	bSizer52->Add( m_staticText19, 0, wxALL, 5 );
	
	m_textCtrl10 = new wxTextCtrl( this, wxID_ANY, wxT("0.3333"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer52->Add( m_textCtrl10, 0, wxALL, 5 );
	
	
	gSizer4->Add( bSizer52, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer9;
	bSizer9 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText20 = new wxStaticText( this, wxID_ANY, wxT("CH2系数"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText20->Wrap( -1 );
	bSizer9->Add( m_staticText20, 0, wxALL, 5 );
	
	m_textCtrl11 = new wxTextCtrl( this, wxID_ANY, wxT("0.3333"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer9->Add( m_textCtrl11, 0, wxALL, 5 );
	
	
	gSizer4->Add( bSizer9, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer10;
	bSizer10 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText21 = new wxStaticText( this, wxID_ANY, wxT("CH3系数"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText21->Wrap( -1 );
	bSizer10->Add( m_staticText21, 0, wxALL, 5 );
	
	m_textCtrl12 = new wxTextCtrl( this, wxID_ANY, wxT("0.3333"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer10->Add( m_textCtrl12, 0, wxALL, 5 );
	
	
	gSizer4->Add( bSizer10, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer11;
	bSizer11 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText22 = new wxStaticText( this, wxID_ANY, wxT("CH4系数"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText22->Wrap( -1 );
	bSizer11->Add( m_staticText22, 0, wxALL, 5 );
	
	m_textCtrl13 = new wxTextCtrl( this, wxID_ANY, wxT("0"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer11->Add( m_textCtrl13, 0, wxALL, 5 );
	
	
	gSizer4->Add( bSizer11, 1, wxEXPAND, 5 );
	
	
	bSizer51->Add( gSizer4, 1, wxEXPAND, 5 );
	
	m_staticText3 = new wxStaticText( this, wxID_ANY, wxT("采样频率"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3->Wrap( -1 );
	bSizer51->Add( m_staticText3, 0, wxALL|wxEXPAND, 5 );
	
	m_dt = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_dt->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INACTIVECAPTIONTEXT ) );
	m_dt->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INACTIVECAPTION ) );
	
	bSizer51->Add( m_dt, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText4 = new wxStaticText( this, wxID_ANY, wxT("数据长度"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText4->Wrap( -1 );
	bSizer51->Add( m_staticText4, 0, wxALL|wxEXPAND, 5 );
	
	m_len = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_len->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INACTIVECAPTIONTEXT ) );
	m_len->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INACTIVECAPTION ) );
	
	bSizer51->Add( m_len, 0, wxALL|wxEXPAND, 5 );
	
	Button1 = new wxButton( this, wxID_ANY, wxT("FFT分析"), wxDefaultPosition, wxDefaultSize, 0 );
	Button1->SetMinSize( wxSize( -1,40 ) );
	
	bSizer51->Add( Button1, 0, wxALL|wxEXPAND, 5 );
	
	
	fgSizer1->Add( bSizer51, 1, wxEXPAND, 5 );
	
	
	bSizer5->Add( fgSizer1, 1, wxEXPAND, 5 );
	
	
	gSizer3->Add( bSizer5, 0, wxEXPAND, 5 );
	
	
	this->SetSizer( gSizer3 );
	this->Layout();
	m_menubar1 = new wxMenuBar( 0 );
	m_menu5 = new wxMenu();
	wxMenuItem* m_menuItem2;
	m_menuItem2 = new wxMenuItem( m_menu5, wxID_ANY, wxString( wxT("说明信息") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu5->Append( m_menuItem2 );
	
	wxMenuItem* m_menuItem3;
	m_menuItem3 = new wxMenuItem( m_menu5, wxID_ANY, wxString( wxT("版本信息") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu5->Append( m_menuItem3 );
	
	m_menubar1->Append( m_menu5, wxT("说明") ); 
	
	this->SetMenuBar( m_menubar1 );
	
	
	this->Centre( wxBOTH );
	
	// Connect Events
	m_filePicker1->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( plc::OnFileChanged ), NULL, this );
	m_filePicker1->Connect( wxEVT_SET_FOCUS, wxFocusEventHandler( plc::SetFocus ), NULL, this );
	m_checkList3->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( plc::Box ), NULL, this );
	m_checkList3->Connect( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, wxCommandEventHandler( plc::BoxDClick ), NULL, this );
	m_checkList3->Connect( wxEVT_COMMAND_CHECKLISTBOX_TOGGLED, wxCommandEventHandler( plc::BoxToggled ), NULL, this );
	Button1->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( plc::OnButtonClick ), NULL, this );
	m_menu5->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( plc::mOnMenuSelection2 ), this, m_menuItem2->GetId());
	m_menu5->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( plc::mOnMenuSelection1 ), this, m_menuItem3->GetId());
}

plc::~plc()
{
	// Disconnect Events
	m_filePicker1->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( plc::OnFileChanged ), NULL, this );
	m_filePicker1->Disconnect( wxEVT_SET_FOCUS, wxFocusEventHandler( plc::SetFocus ), NULL, this );
	m_checkList3->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( plc::Box ), NULL, this );
	m_checkList3->Disconnect( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, wxCommandEventHandler( plc::BoxDClick ), NULL, this );
	m_checkList3->Disconnect( wxEVT_COMMAND_CHECKLISTBOX_TOGGLED, wxCommandEventHandler( plc::BoxToggled ), NULL, this );
	Button1->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( plc::OnButtonClick ), NULL, this );
	
}
