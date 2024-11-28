import subprocess

for script in ["client.py", "server.py"]:
    subprocess.Popen(
        ["start", "python", script],
        shell=True  # Обязательно для открытия новых окон в Windows
    )