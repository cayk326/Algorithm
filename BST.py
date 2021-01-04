class Node(object):
    '''
    節クラス
        ノード
      ／      ＼
    左エッジ   右エッジ
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    '''
    各親とそれに紐づく子供を抽出した際に
    左の子 <= 親 < 右の子が成り立つ木
    '''
    def __init__(self):
        self.root = None

    '''
    木の最小値を返す
    '''
    def get_min(self):
        if self.root:
            return self._get_min(self.root)
        return False

    def _get_min(self, node):
        if node.left:
            return self._get_min(node.left)
        return node.data

    '''
    木の最大値を返す
    '''
    def get_max(self):
        if self.root:
            return self._get_max(self.root)
        return False

    def _get_max(self, node):
        if node.right:
            return self._get_max(node.right)
        return node.data

    def insert(self, data):
        '''
        挿入対象データを木に挿入する
        _insertが挿入ロジックの本体で、insertは木にノードが存在しない際の
        処理を記載
        :param data:
        :return:
        '''
        # rootに何もノードが存在しない場合
        if not self.root:
            self.root = Node(data)
        # rootに値が存在する場合は適切な場所に値を挿入する関数を実行
        else:
            self._insert(self.root, data)# 木全体と挿入したいデータを渡す

    # 挿入にかかるコストは木が平衡していればO(log(N))　一直線に伸びているような場合はO(N)
    def _insert(self, node, data):
        '''
        挿入対象データを木に挿入する
        :param node:
        :param data:
        :return:
        '''
        # あるノードのデータと挿入したいデータを比較して挿入したいデータのほうが小さいもしくは同じとき
        if data <= node.data:
            # ノードの左の子が存在する場合はさらに調査
            if node.left:
                self._insert(node.left, data)
            # ノードの左の子がNoneならこの場所に追加
            else:
                node.left = Node(data)
        # あるノードのデータと挿入したいデータを比較して挿入したいデータのほうが大きい時
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)


    def dfs_inorder(self, tree):
        '''
        行きがけ順の深さ優先探索
        ソートされた値を表示できる

        1. 左下に再帰的に潜れるだけ潜る
        2. 左最下層の値を表示
        3. 一個前のノードに戻る
        4. 現在の値を表示
        5. 右に一個潜る
        6. 左に潜れそうならいけるだけ潜る
        7. 最下層で値を表示
        8. 3に戻る
        :param tree:
        :return:
        '''
        node = tree
        # 木に何も存在しないとき
        if node is None:
            print("No data")
            return
        # 存在するとき
        else:
            # 左下に潜れるだけ潜る
            if node.left:
                self.dfs_inorder(node.left)
            # 表示
            print(node.data)
            # 右に潜れるだけ潜る
            if node.right:
                self.dfs_inorder(node.right)










if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(14)
    bst.insert(4)
    bst.insert(7)
    bst.insert(13)
    print(bst.get_max())
    print(bst.get_min())
    print()
    bst.dfs_inorder()