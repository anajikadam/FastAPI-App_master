import uvicorn
UVI_APP_HOST = 'localhost'
UVI_APP_PORT = 8085

if __name__ == '__main__':
    print("App Started...!!!!!")
    uvicorn.run("main:app",  
                host=UVI_APP_HOST,
                port=UVI_APP_PORT, 
                reload = True,
    )
                # limit_concurrency=3)
    