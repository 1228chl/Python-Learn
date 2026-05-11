# git_proxy_gui.py
import subprocess
import shutil
import sys
import platform
import tkinter as tk
from tkinter import messagebox, ttk

class GitProxyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Git代理管理器")
        self.root.geometry("520x350")
        self.root.resizable(False, False)

        # 变量
        self.protocol_var = tk.StringVar(value="http")
        self.host_var = tk.StringVar(value="127.0.0.1")
        self.port_var = tk.StringVar(value="7897")
        self.status_var = tk.StringVar(value="就绪")
        self.http_label_var = tk.StringVar()
        self.https_label_var = tk.StringVar()

        self.create_widgets()
        self.check_git_or_exit()
        self.refresh_proxy_display()

    def check_git_or_exit(self):
        """检测 Git 是否可用，不可用则退出"""
        if not shutil.which("git"):
            messagebox.showerror("错误", "未找到 Git 命令！\n请确保 Git 已安装并添加到 PATH 环境变量中。")
            self.root.destroy()
            sys.exit(1)

    def run_git_command(self, args):
        """执行 git config 命令，完全隐藏窗口（Windows）"""
        try:
            # 针对 Windows 隐藏子进程控制台窗口
            if platform.system() == "Windows":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
                creationflags = subprocess.CREATE_NO_WINDOW
            else:
                startupinfo = None
                creationflags = 0

            result = subprocess.run(
                ["git"] + args,
                capture_output=True,
                text=True,
                check=False,
                startupinfo=startupinfo,
                creationflags=creationflags
            )
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        except Exception as e:
            return "", str(e), -1

    def get_proxy(self):
        """获取当前 http.proxy 和 https.proxy 值"""
        http_out, _, _ = self.run_git_command(["config", "--global", "--get", "http.proxy"])
        https_out, _, _ = self.run_git_command(["config", "--global", "--get", "https.proxy"])
        return (http_out if http_out else None, https_out if https_out else None)

    def refresh_proxy_display(self):
        """刷新界面显示的代理状态"""
        http_proxy, https_proxy = self.get_proxy()
        self.http_label_var.set(f"HTTP 代理: {http_proxy if http_proxy else '未设置'}")
        self.https_label_var.set(f"HTTPS 代理: {https_proxy if https_proxy else '未设置'}")
        self.status_var.set("状态已刷新")

    def build_proxy_url(self):
        """从协议、主机、端口构建完整的代理 URL"""
        protocol = self.protocol_var.get().strip().lower()
        host = self.host_var.get().strip()
        port = self.port_var.get().strip()

        if not host:
            return None
        if not port:
            return None

        # 确保协议以 :// 结尾
        if not protocol.endswith("://"):
            proxy_url = f"{protocol}://{host}:{port}"
        else:
            proxy_url = f"{protocol}{host}:{port}"
        return proxy_url

    def set_proxy(self, proxy):
        """同时设置 http.proxy 和 https.proxy"""
        if not proxy:
            messagebox.showwarning("警告", "代理地址不能为空！")
            return False

        # 设置 http.proxy
        _, stderr, code = self.run_git_command(["config", "--global", "http.proxy", proxy])
        if code != 0:
            messagebox.showerror("错误", f"设置 HTTP 代理失败:\n{stderr}")
            return False

        # 设置 https.proxy
        _, stderr, code = self.run_git_command(["config", "--global", "https.proxy", proxy])
        if code != 0:
            messagebox.showerror("错误", f"设置 HTTPS 代理失败:\n{stderr}")
            return False

        self.status_var.set(f"代理已开启: {proxy}")
        self.refresh_proxy_display()
        return True

    def enable_proxy(self):
        """开启代理（从输入框读取协议、主机、端口）"""
        proxy = self.build_proxy_url()
        if not proxy:
            messagebox.showwarning("警告", "请完整填写代理主机地址和端口！")
            return
        self.set_proxy(proxy)

    def disable_proxy(self):
        """关闭代理（删除全局 http.proxy 和 https.proxy）"""
        self.run_git_command(["config", "--global", "--unset", "http.proxy"])
        self.run_git_command(["config", "--global", "--unset", "https.proxy"])
        self.status_var.set("代理已关闭")
        self.refresh_proxy_display()

    def create_widgets(self):
        # 说明标签
        info_label = tk.Label(
            self.root,
            text="支持 http / https / socks5 等协议，填写主机和端口后自动组合为代理地址",
            fg="gray", justify="left"
        )
        info_label.pack(pady=(10, 0), padx=10, anchor="w")

        # 代理配置区域（协议、主机、端口）
        frame_config = ttk.LabelFrame(self.root, text="代理设置", padding="8")
        frame_config.pack(pady=10, padx=10, fill="x")

        # 协议选择
        ttk.Label(frame_config, text="协议:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        protocol_combo = ttk.Combobox(frame_config, textvariable=self.protocol_var, width=10, state="readonly")
        protocol_combo['values'] = ('http', 'https', 'socks5')
        protocol_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # 主机地址
        ttk.Label(frame_config, text="主机地址:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        host_entry = ttk.Entry(frame_config, textvariable=self.host_var, width=20)
        host_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # 端口
        ttk.Label(frame_config, text="端口:").grid(row=0, column=4, padx=5, pady=5, sticky="w")
        port_entry = ttk.Entry(frame_config, textvariable=self.port_var, width=8)
        port_entry.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        # 开启/关闭按钮
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10, padx=10, fill="x")
        tk.Button(frame_buttons, text="开启代理", command=self.enable_proxy, bg="#c7e9ff", width=12).pack(side="left", padx=5)
        tk.Button(frame_buttons, text="关闭代理", command=self.disable_proxy, bg="#ffd9d9", width=12).pack(side="left", padx=5)

        # 状态显示区域
        frame_display = ttk.LabelFrame(self.root, text="当前 Git 代理状态", padding="8")
        frame_display.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(frame_display, textvariable=self.http_label_var, anchor="w", fg="#2c3e50").pack(anchor="w", pady=2)
        tk.Label(frame_display, textvariable=self.https_label_var, anchor="w", fg="#2c3e50").pack(anchor="w", pady=2)

        tk.Button(frame_display, text="🔄 刷新", command=self.refresh_proxy_display, width=10).pack(pady=8)

        # 底部状态栏
        status_bar = tk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w", bd=1)
        status_bar.pack(side="bottom", fill="x")

if __name__ == "__main__":
    root = tk.Tk()
    app = GitProxyGUI(root)
    root.mainloop()