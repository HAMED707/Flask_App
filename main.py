from website import creat_app ,db

app = creat_app()

if __name__=="__main__":
         # Create tables
        with app.app_context():
                db.create_all()
        print("Database created!")
        app.run(debug=True)