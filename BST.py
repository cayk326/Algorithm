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






if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(5)
    bst.insert(3)
    bst.insert(5)
    print()