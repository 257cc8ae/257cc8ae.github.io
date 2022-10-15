from datetime import date
contest_name = input("コンテストの名前を入力してください。(ex)ABC001 ⇛ abc001 : ")
problem_number = input("問題名を入力してください。(ex)ABC001のA問題の場合 ⇛ a : ")
submission_url = input("提出コードのURLを入力してください : ")

cn = contest_name.upper()
pm = problem_number.upper()

try:
    with open(f"records/{contest_name}_{problem_number}.md", mode='x') as f:
        f.write(
            f"""### [{cn} - {pm}](https://atcoder.jp/contests/{contest_name}/tasks/{contest_name}_{problem_number})
            
[提出]({submission_url})

{date.today()}
            """
        )
except FileExistsError:
    pass

with open("index.md", mode='a') as f:
    f.write(f'\n| [{cn} - {pm}](records/{contest_name}_{problem_number}.md) | {date.today()} | [提出結果]({submission_url}) |')
