class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def set_val(self, data):
        self.data = data

    def get_val(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SingleLinkedList():
    # 連結リストの長さを取得
    # 先頭ノードの生成
    # ノードの追加
    # ノードの削除
    # ノードの検索

    # 連結リストの初期化
    def __init__(self):
        self.head = None
        self.length = 0

    # 連結リストの長さ、ノード数を計算
    def length_list(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.get_next()
        return length

    # 連結リストの中身を表示する
    def print_linked_list(self):
        print()
        # 連結リストの先頭のノードをtempとして格納
        temp = self.head
        # tempがNoneじゃない間はループ
        while temp:
            print("Node value is:", temp.data)
            # tempを次のノードのポインタにする
            temp = temp.next

    # 連結リストのノードにある値が存在するか検索する
    def search(self, node, data):
        # ノードに何も存在しなければ終了
        if node is None:
            return False
        # ノードの中のデータと検索対象のデータが一致した場合Trueを返す
        if node.data == data:
            return True
        # 再帰処理。連結リストを先頭から末尾までたどりながら、dataと一致するものを探す。
        # 連結リストの大きな特徴となる部分。追加や削除はしやすいがO(1)、検索はO(N)かかる
        # 挿入や削除する位置を検索するために探索をしないといけない場合も多々あり
        # データの追加や削除が多発する場合は連結リストがおすすめ
        return self.search(node.get_next(), data)

    # 連結リストの先頭に新しく作ったノードを追加する
    def insert_node_at_start(self, data):
        # length = self.length_list()
        new_node = Node(data)
        # Headに何もない=連結リストの中身が存在しない空の状態の時
        if List.head == None:
            # 新しく作ったNode(data, next)をHeadとして登録する
            self.head = new_node
        else:
            # 既に連結リストのHeadが存在するとき
            # 新しいノードを先頭につなげるために、新しく作ったノードの
            # nextを現状のHeadにする。つまり、ノードを先頭から追加している。
            new_node.set_next(self.head)
            # Headを新しく作ったノードとして再登録する
            self.head = new_node
        # 連結リストのノード数が増えたので長さを加算
        self.length += 1

    # 連結リストの末尾にノードを追加する。ノードが存在しないときはエラーを出力
    def insert_node_at_end(self, data):
        # 連結リストのノードが存在しないときにはエラーを出力。末尾につなげるノードが無い
        if List.head == None:
            print("Do not add node at end position. You need to add node using insert_node_at_start")
            return -1
        else:
            # 新しいノードを生成
            new_node = Node(data)
            # 連結リストの先頭ノードをtempに格納
            temp = self.head
            # tempのnextポインタがNoneじゃない間はループ。
            while temp.get_next() is not None:
                # tempにnextの値を入れている。つまり連結リストの末尾まで移動している
                temp = temp.get_next()
            # 連結リストの末尾のnextに新しく生成したノードの情報を格納
            # self.nextではないことに注意。ここでの変更がListにきちんと反映される
            temp.next = new_node
            # ノードが増えたので長さを増やす
            self.length += 1

    # 連結リストの任意の位置にノードを挿入する
    def insert_position(self, position, data):
        # ノードを挿入する位置が0より小さいもしくは連結リストの長さより大きいときは
        # 挿入できない
        if position < 0 or position > self.length:
            raise ValueError

        else:
            # 挿入する位置が0、すなわち先頭の時
            if position == 0:
                # 先頭にノードを挿入するための関数を実行
                self.insert_node_at_start(data)
            # 挿入する位置がself.length、すなわち連結リストの終端の時
            elif position == self.length:
                # 終端にノードを挿入するための関数を実行
                self.insert_node_at_end(data)
            # ノードとノードの間に挿入するとき
            else:
                # 連結リスト終端の位置
                length = self.length_list()
                # 新しいノード
                new_node = Node(data)
                count = 0
                # 連結リストの先頭
                temp = self.head
                # 挿入したい部分までループ
                while count < position - 1:
                    count += 1
                    # 連結リストを走査
                    temp = temp.get_next()
                # 新しく生成したノードのnextに次のノードの位置を記録
                new_node.set_next(temp.get_next())
                # 現在のノードのnextには新しく生成したノードの位置を記録
                temp.set_next(new_node)
                # ノードが増えたので長さを増やす
                self.length = length + 1

    # 連結リストのノードを削除する
    def delete_node(self, data):
        # 連結リストの長さを取得
        length = self.length_list()
        temp = self.head
        # 次のノードに何かある場合
        if temp.next is not None:
            # temp.dataが対象のdataと一致する場合
            if temp.data == data:
                # headに現在のノードの次のノードの情報を入れる。連結の組み換え
                self.head = temp.get_next()
                # 現在のノードの情報はなくす
                temp = None
                # 連結リストのノードを消したので1減らす
                self.length = length - 1
            # temp.dataが対象のdataと一致しないとき
            else:
                # 連結リストの末尾まで走査
                while temp.next is not None:
                    # もしdataと一致するノードを見つけたらブレイク
                    if temp.data == data:
                        break
                    # temp(すなわちheadの情報)をprevに退避
                    prev = temp
                    # tempにはtemp(現在のノード)の次のノードを格納
                    temp = temp.get_next()
                    # tempには何もない場合、すなわち検索対象の値が連結リストに存在しないとき

                if temp.next is None:
                    print("Cannot find target value in linked list")
                    return
                # ノードを繋ぎ変える
                prev.next = temp.get_next()
                temp = None
                # 長さを減らす
                self.length = length - 1
        return


if __name__ == '__main__':
    List = SingleLinkedList()
    List.insert_node_at_end(50)
    List.print_linked_list()
    List.insert_node_at_start(1)
    List.print_linked_list()
    List.insert_node_at_start(20)
    List.print_linked_list()
    List.insert_node_at_end(30)
    List.print_linked_list()
    List.insert_position(1, 600)
    List.print_linked_list()
    List.delete_node(1)
    List.print_linked_list()
    List.delete_node(1)
    List.print_linked_list()