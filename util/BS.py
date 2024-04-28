import os
import requests
import json

boj_base_url = "https://www.acmicpc.net/problem/"


def get_problem_info(link):
    tlink = link.split("/")
    if len(tlink) != 5:
        print(
            "wrong address - address format should be https://www.acmicpc.net/problem/xxx"
        )
        return

    problem_id = tlink[4]
    if not problem_id.isdigit():
        print("wrong address")
        return
    boj_problem_api_url = "https://solved.ac/api/v3/problem/show"
    query_string = {"query": " ", "problemId": f"{problem_id}"}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "GET", boj_problem_api_url, headers=headers, params=query_string
    )
    if response.ok:
        print("-----successfully got problem info-----")
        temp_problem_json = json.loads(response.text)
        problem_title = str(temp_problem_json.get("titleKo"))
        return int(problem_id), problem_title
    else:
        print("failed get problem info")
    return 0, None


def get_problem_info_detail(problem_id):
    if not problem_id.isdigit():
        print("wrong address")
        return
    boj_problem_api_url = "https://solved.ac/api/v3/problem/show"
    query_string = {"query": " ", "problemId": f"{problem_id}"}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "GET", boj_problem_api_url, headers=headers, params=query_string
    )
    if response.ok:
        print("-----successfully got problem info-----")
        temp_problem_json = json.loads(response.text)
        problem_info_detail = temp_problem_json
        return int(problem_id), problem_info_detail
    else:
        print("failed get problem info")
    return 0, None


def make_file_all(problem_list, program_dir, platform):
    print("current directory:")
    print("##" + os.getcwd() + "##")
    file_extension = "cpp"
    if len(problem_list) != 0:
        for problem_id, problem_title in problem_list:
            print("------------------------------------------------------------")
            print("problem id: " + str(problem_id))
            print("problem title: " + problem_title)
            file_name = str(problem_id) + "." + file_extension
            if os.path.isfile(file_name):
                print("problem file already exist")
            else:
                # TODO make snippet to txt file and read them to make
                f = open(file_name, "w", encoding="UTF-8")
                if platform == "darwin":
                    t = open(program_dir + "/snippets/c++.txt", "r", encoding="UTF-8")
                else:
                    t = open(program_dir + "\snippets\c++.txt", "r", encoding="UTF-8")
                cnt = 0
                while True:
                    line = t.readline()
                    if not line:
                        break
                    if cnt == 0:
                        f.write(line.split("\n")[0] + problem_title + "\n")
                    elif cnt == 1:
                        f.write(line.split("\n")[0] + str(problem_id) + "\n")
                    else:
                        f.write(line)
                    cnt += 1


def make_file(problem_id, problem_title, program_dir, platform):
    print("current directory:")
    print("##" + os.getcwd() + "##")
    file_extension = ""
    while True:
        print("select language (1: cpp, 2: python)")
        sl = int(input())
        if sl == 1:
            file_extension = "cpp"
            break
        elif sl == 2:
            file_extension = "py"
            break
        else:
            print("wrong input")
    if problem_id != 0 and problem_title != None:
        file_name = str(problem_id) + "." + file_extension
        if os.path.isfile(file_name):
            print("problem file already exist")
        else:
            # TODO make snippet to txt file and read them to make
            f = open(file_name, "w", encoding="UTF-8")
            if file_extension == "cpp":
                # f.write("// problem: " + problem_title + "\n")
                # f.write("// id: " + str(problem_id) + "\n")
                # f.write("// time taken:\n")
                # f.write("#include <bits/stdc++.h>\n")
                # f.write("using namespace std;\n")
                # f.write("int main(void)\n")
                # f.write("{\n")
                # f.write("    ios::sync_with_stdio(false);\n")
                # f.write("    cin.tie(nullptr);\n")
                # f.write("\n")
                # f.write("    return 0;\n")
                # f.write("}\n")
                if platform == "darwin":
                    t = open(program_dir + "/snippets/c++.txt", "r", encoding="UTF-8")
                else:
                    t = open(program_dir + "\snippets\c++.txt", "r", encoding="UTF-8")
                cnt = 0
                while True:
                    line = t.readline()
                    if not line:
                        break
                    if cnt == 0:
                        f.write(line.split("\n")[0] + problem_title + "\n")
                    elif cnt == 1:
                        f.write(line.split("\n")[0] + str(problem_id) + "\n")
                    else:
                        f.write(line)
                    cnt += 1

            elif file_extension == "py":
                f.write("# problem: " + problem_title + "\n")
                f.write("# id: " + str(problem_id) + "\n")
                f.write("# time taken:")
            f.close()

    else:
        print("problem unsellected")
