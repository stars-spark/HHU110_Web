from flask import Flask, request, jsonify
from flask_cors import CORS
from models import get_session, History, Discipline, Message, User

app = Flask(__name__)
CORS(app)  # 允许本地跨域调试

@app.get("/api/ping")
def ping():
    return jsonify({"msg": "pong"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)


@app.get("/api/history")
def list_history():
    year = request.args.get("year")
    page = int(request.args.get("page", 1))
    size = int(request.args.get("page_size", 10))
    session, _ = get_session()
    q = session.query(History).order_by(History.year)
    if year:
        q = q.filter(History.year == int(year))
    total = q.count()
    items = q.offset((page-1)*size).limit(size).all()
    data = [{"id":i.id,"year":i.year,"title":i.title,"content":i.content,"cover_url":i.cover_url} for i in items]
    session.close()
    return jsonify({"list": data, "total": total})

@app.get("/api/disciplines")
def list_disciplines():
    session, _ = get_session()
    items = session.query(Discipline).all()
    data = [{"id":i.id,"name":i.name,"intro":i.intro,"icon":i.icon} for i in items]
    session.close()
    return jsonify(data)

@app.get("/api/messages")
def list_messages():
    page = int(request.args.get("page", 1))
    size = int(request.args.get("page_size", 10))
    session, _ = get_session()
    q = session.query(Message).order_by(Message.created_at.desc())
    total = q.count()
    items = q.offset((page-1)*size).limit(size).all()
    data = [{"id":m.id,"user":m.user.username,"content":m.content,"likes":m.likes,"created_at":m.created_at.isoformat()} for m in items]
    session.close()
    return jsonify({"list": data, "total": total})

@app.post("/api/messages")
def create_message():
    j = request.get_json(force=True)
    content = (j.get("content") or "").strip()
    if not content:
        return jsonify({"ok": False, "code":"INVALID_PARAM", "msg":"内容不能为空"}), 400
    session, _ = get_session()
    user = session.query(User).first()
    msg = Message(user=user, content=content)
    session.add(msg); session.commit()
    r = {"ok": True, "id": msg.id}
    session.close()
    return jsonify(r), 201

@app.post("/api/messages/<int:mid>/like")
def like_message(mid):
    session, _ = get_session()
    msg = session.query(Message).get(mid)
    if not msg:
        session.close()
        return jsonify({"ok": False, "code":"NOT_FOUND", "msg":"不存在"}), 404
    msg.likes += 1
    session.commit()
    r = {"ok": True, "likes": msg.likes}
    session.close()
    return jsonify(r)
