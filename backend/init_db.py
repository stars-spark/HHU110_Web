from models import Base, get_session, History, Discipline, User, Message

def init():
    session, engine = get_session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # 演示数据
    session.add_all([
        History(year=1915, title="校史起点", content="……"),
        History(year=1958, title="重要事件", content="……"),
    ])
    session.add_all([
        Discipline(name="水利工程", intro="河海特色……"),
        Discipline(name="物联网工程", intro="新工科……"),
    ])
    u = User(username="匿名用户")
    session.add(u)
    session.add(Message(user=u, content="青春河海，加油！"))
    session.commit()
    print("DB initialized.")

if __name__ == "__main__":
    init()
