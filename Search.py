def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 左端と右端のindex
    index_left, index_right = 0, len(sorted_array) - 1

    # 二分探索
    while index_left <= index_right: # 左端のindexが右端のindexを追い越すまで繰り返す

        # 中央のindex
        index_middle = (index_left + index_right) // 2

        # 中央のindexに対する配列の値と探索対象の番号を比較
        if sorted_array[index_middle] == target_number:
            # もし一致するならその中央のindexが答えとなる
            return index_middle
        elif sorted_array[index_middle] < target_number:
            # 配列の値が小さい場合はそれ以下の部分は探索する必要がないので
            # 左端のindexを「中央のindex+1」に変更し、探索範囲を絞る
            index_left = index_middle + 1
        elif sorted_array[index_middle] > target_number:
            # 配列の値が大きい場合はそれ以上の部分は探索する必要がないので
            # 右端のindexを「中央のindex-1」に変更し、探索範囲を絞る
            index_right = index_middle - 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()