import uuid, os
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse # 新增这个导入

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

if not os.path.exists("static_md"):
    os.makedirs("static_md")

# 修改这里：普通的 mount 只是为了让文件能被访问
app.mount("/static", StaticFiles(directory="static_md"), name="static")

@app.post("/generate_md")
async def generate_md(content: str = Form(...)):
    try:
        # 清洗一下 AI 可能带出来的奇怪转义
        clean_content = content.replace('\\n', '\n').replace('\\"', '"')
        
        file_name = f"{uuid.uuid4()}.md"
        file_path = f"static_md/{file_name}"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(clean_content)
        
        # 返回链接，我们在 URL 后面加个参数，虽然不是必须，但方便识别
        # download_url = f"http://192.168.137.52:8001/download/{file_name}"
        download_url = f"http://192.168.58.187:8001/download/{file_name}"
        return {"markdown_url": download_url}

    except Exception as e:
        print(f"8001 报错: {e}")
        return {"error": str(e)}

# --- 新增：专门的强制下载接口 ---
@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = f"static_md/{file_name}"
    if os.path.exists(file_path):
        # filename 参数会触发浏览器的“另存为”对话框
        return FileResponse(
            path=file_path, 
            filename=f"诊断报告_{file_name[:8]}.md", 
            media_type='application/octet-stream'
        )
    return {"error": "文件不存在"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)