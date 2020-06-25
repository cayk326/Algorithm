'''
postorder traversal method

'''

def DS(pos):
    print('Execute depth search post order')
    for i in tree[pos]:# 探索ノードの配下にあるノードを検索
        DS(i)#再帰的に探索
    print(pos, end='\n')  # 配下のノードを調べた後に出力(処理)


if __name__ == '__main__':
    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [], [], [], [], [], [], [], []]

    DS(0)