# check_audio_permissions.py
import os
import platform
import subprocess


def check_windows_audio_permissions():
    """检查Windows音频权限"""
    print("=== 检查Windows音频权限 ===")

    if platform.system() != "Windows":
        print("非Windows系统，跳过权限检查")
        return

    try:
        # 检查音频服务是否运行
        result = subprocess.run(
            ['sc', 'query', 'Audiosrv'],
            capture_output=True,
            text=True
        )
        if "RUNNING" in result.stdout:
            print("✓ Windows音频服务正在运行")
        else:
            print("✗ Windows音频服务未运行")

        # 检查默认音频设备
        result = subprocess.run(
            ['powershell', '-Command', 'Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status'],
            capture_output=True,
            text=True
        )
        print("音频设备信息:")
        print(result.stdout)

    except Exception as e:
        print(f"权限检查错误: {e}")


def check_firewall_and_network():
    """检查防火墙和网络设置"""
    print("\n=== 检查网络设置 ===")

    try:
        # 测试连接到微软TTS服务
        import urllib.request
        import ssl

        # 跳过SSL验证（测试用）
        ssl._create_default_https_context = ssl._create_unverified_context

        # 测试连接
        response = urllib.request.urlopen(
            'https://speech.platform.bing.com/',
            timeout=10
        )
        print(f"✓ 可以连接到微软TTS服务 (状态码: {response.getcode()})")

    except Exception as e:
        print(f"✗ 网络连接问题: {e}")
        print("建议: 检查防火墙设置或尝试使用VPN")


if __name__ == "__main__":
    check_windows_audio_permissions()
    check_firewall_and_network()