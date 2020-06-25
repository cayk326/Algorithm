'''
inorder traversal method

'''

def DS(pos):
    print('Execute depth search in order')
    if len(tree[pos]) == 2: # 子が二つあるとき
        DS(tree[pos][0])# 左のノードを再帰的に調べる
        print(pos, end='\n')# 左のノードと右のノードの間に出力(実行)
        DS(tree[pos][1])# 右のノードを再帰的に調べる

    elif len(tree[pos]) == 1:# 子が一つの時。つまり左側ノードのみ存在
        DS(tree[pos][0])# 左のノードを再帰的に調べる
        print(pos, end='\n')  # 左のノードを調べた後に出力(実行)

    else:# 子が一つもなかったら
        print(pos, end='\n')

if __name__ == '__main__':
    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [], [], [], [], [], [], [], []]

    DS(0)