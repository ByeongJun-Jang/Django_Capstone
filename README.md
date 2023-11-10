# Django_Capstone 

Description  
- 유저의 회원가입, 로그인 기능
- 게시판
- 시간표 작성
- 시간표 데이터베이스 모델 구축 X
  
Model Compositoin
```
Accounts { // ceo_accounts 동일
	id: number;        
	username: string;  
	useremail: string; 
  password: string;  
  created_at: date;  
}

Boards {  // ceo_boards 동일
    id: number;       
    contents: string; 
    title: string;    
    writer:; 
    created_at: date; 
    updated_at: date; 
}

Timetable{  // ceo_timetable 동일
  id: number;
  username: string;
  open_mon: boolean;
  mid_mon: boolean;
  '''
  '''
  '''
  mid_sun: boolean;
  close_sun: boolean;
}
```

Environments
```
python3 --version
Python 3.10.7

python3 -m django --version
4.2.5
```

Project
```
project capde
-------------
capde
├── capde
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── accounts
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── ceoaccounts
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── boards
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── ceoboards
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── profileapp
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── timetable
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── ceotimetable
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
    
Execution
```
> cd capde

> python3 manage.py runserver
```
