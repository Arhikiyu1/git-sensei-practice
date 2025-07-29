import google.generativeai as genai
import subprocess

# APIキーを設定
genai.configure(api_key="YOURE_API_KEY")
model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

# git diffの出力を取得
diff_output = subprocess.check_output(["git", "diff", "--staged"]).decode("utf-8")

if not diff_output.strip():
    print("ステージングされた変更はありません。")
else:
    prompt = f"""
    あなたはエキスパートのソフトウェア開発者です。
    以下のgit diffを分析し、Conventional Commits仕様に準拠したコミットメッセージを生成してください。

    ---
    例1:
    diff:
    --- a/main.py
    +++ b/main.py
    -    print("Hllo, World!")
    +    print("Hello, World!")

    コミットメッセージ:
    fix: correct typo in greeting message

    ---
    例2:
    diff:
    --- a/auth.py
    +++ b/auth.py
    +def login(username, password):
    +    #... login logic...
    +    return True

    コミットメッセージ:
    feat(auth): add basic login function

    ---
    実際のdiff:
    {diff_output}

    ---
    コミットメッセージ:
    """

    response = model.generate_content(prompt)
    print(response.text)
