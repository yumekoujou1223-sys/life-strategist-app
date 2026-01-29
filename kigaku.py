# -*- coding: utf-8 -*-
"""
九星気学計算エンジン
本命星と現在の座相を計算
"""

# 九星の定義
NINE_STARS = {
    1: "一白水星",
    2: "二黒土星",
    3: "三碧木星",
    4: "四緑木星",
    5: "五黄土星",
    6: "六白金星",
    7: "七赤金星",
    8: "八白土星",
    9: "九紫火星"
}

# 九宮の定義
NINE_PALACES = {
    1: "坎宮（北）",
    2: "坤宮（南西）",
    3: "震宮（東）",
    4: "巽宮（南東）",
    5: "中宮（中央）",
    6: "乾宮（北西）",
    7: "兌宮（西）",
    8: "艮宮（北東）",
    9: "離宮（南）"
}

def calculate_honmei_star(year, month, day):
    """
    本命星を計算
    注意: 1月1日〜節分（2月3日頃）は前年扱い
    """
    # 節分前なら前年として扱う
    if month == 1 or (month == 2 and day <= 3):
        year -= 1
    
    # 1901年を基準年とする（1901年=九紫火星）
    # 九星は9年周期で逆回転（毎年1ずつ減少）
    base_year = 1901
    base_star = 9  # 1901年の本命星
    
    year_diff = year - base_year
    star = base_star - (year_diff % 9)
    
    if star <= 0:
        star += 9
    
    return star

def calculate_current_position(honmei_star, current_year):
    """
    現在の座相（宮）を計算
    年盤における本命星の位置
    """
    # 2026年の年盤中央は七赤金星
    # 年盤は毎年変わる（9年周期）
    base_year = 2026
    base_center = 7  # 2026年の中央星
    
    year_diff = current_year - base_year
    current_center = base_center - (year_diff % 9)
    
    if current_center <= 0:
        current_center += 9
    
    # 本命星が中央からどの位置にあるかを計算
    # 九星盤の配置パターン（中央を基準に）
    position_map = {
        0: 5,  # 中央
        1: 6, 2: 2, 3: 4, 4: 9, 5: 1, 6: 8, 7: 3, 8: 7
    }
    
    diff = (honmei_star - current_center) % 9
    position = position_map.get(diff, 5)
    
    return position

def get_position_description(position):
    """
    座相の説明を取得
    """
    descriptions = {
        1: "坎宮（冬・水の時期）- 静かに力を蓄える、内省と準備の時",
        2: "坤宮（大地・母性）- 周囲をサポート、基盤を固める時",
        3: "震宮（春・雷）- 新しい挑戦を始める、行動開始の時",
        4: "巽宮（風・調整）- 人間関係を広げ、情報を集める時",
        5: "中宮（中心・停滞）- 慎重に行動、自己を見つめ直す時",
        6: "乾宮（天・権威）- リーダーシップを発揮、目標達成の時",
        7: "兌宮（秋・収穫）- 成果を楽しむ、コミュニケーションの時",
        8: "艮宮（山・変化）- 転換期、新しい方向性を模索する時",
        9: "離宮（夏・頂点）- 最も運気が高まる、表舞台に立つ時"
    }
    return descriptions.get(position, "")

def get_kigaku_profile(year, month, day, current_year=2026):
    """
    完全な九星気学プロファイルを取得
    """
    honmei = calculate_honmei_star(year, month, day)
    position = calculate_current_position(honmei, current_year)
    
    return {
        'honmei_star': honmei,
        'honmei_name': NINE_STARS[honmei],
        'current_position': position,
        'position_name': NINE_PALACES[position],
        'position_description': get_position_description(position)
    }

if __name__ == "__main__":
    # テスト
    result = get_kigaku_profile(1960, 12, 23, 2026)
    print("九星気学プロファイル:", result)
