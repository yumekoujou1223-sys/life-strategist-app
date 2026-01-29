# -*- coding: utf-8 -*-
"""
数秘術計算エンジン
ライフパス、デスティニー、ソウル、パーソナルイヤーを計算
"""

def reduce_to_single_digit(n, keep_master=True):
    """
    数字を一桁に還元（マスターナンバー11, 22, 33は保持）
    """
    while n > 9:
        if keep_master and n in [11, 22, 33]:
            return n
        n = sum(int(digit) for digit in str(n))
    return n

def calculate_life_path(year, month, day):
    """
    ライフパスナンバー（LP）を計算
    生年月日の合計から算出
    """
    # 年月日をそれぞれ還元してから合計
    year_sum = reduce_to_single_digit(year)
    month_sum = reduce_to_single_digit(month)
    day_sum = reduce_to_single_digit(day)
    
    total = year_sum + month_sum + day_sum
    return reduce_to_single_digit(total)

def char_to_number(char):
    """
    アルファベットを数字に変換（ピタゴラス式）
    A=1, B=2, ..., I=9, J=1, ...
    """
    char = char.upper()
    if not char.isalpha():
        return 0
    return ((ord(char) - ord('A')) % 9) + 1

def calculate_destiny(name):
    """
    デスティニーナンバー（D）を計算
    フルネームの全文字の合計
    """
    total = sum(char_to_number(c) for c in name if c.isalpha())
    return reduce_to_single_digit(total)

def calculate_soul(name):
    """
    ソウルナンバー（S）を計算
    母音のみの合計
    """
    vowels = 'AEIOU'
    total = sum(char_to_number(c) for c in name.upper() if c in vowels)
    return reduce_to_single_digit(total)

def calculate_personal_year(year, month, day, current_year):
    """
    パーソナルイヤーナンバー（P）を計算
    誕生日の月日 + 現在の年
    """
    month_sum = reduce_to_single_digit(month)
    day_sum = reduce_to_single_digit(day)
    year_sum = reduce_to_single_digit(current_year)
    
    total = month_sum + day_sum + year_sum
    return reduce_to_single_digit(total)

def get_numerology_profile(year, month, day, name, current_year=2026):
    """
    完全な数秘術プロファイルを取得
    """
    lp = calculate_life_path(year, month, day)
    d = calculate_destiny(name)
    s = calculate_soul(name)
    p = calculate_personal_year(year, month, day, current_year)
    
    return {
        'life_path': lp,
        'destiny': d,
        'soul': s,
        'personal_year': p
    }

if __name__ == "__main__":
    # テスト
    result = get_numerology_profile(1960, 12, 23, "WASSHI", 2026)
    print("数秘術プロファイル:", result)
