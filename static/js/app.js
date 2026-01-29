// ========================================
// アプリケーションメインロジック
// ========================================

// ステップ管理
const steps = {
    welcome: document.getElementById('step-welcome'),
    loading: document.getElementById('step-loading'),
    result: document.getElementById('step-result')
};

// 現在のステップを切り替える
function showStep(stepName) {
    Object.values(steps).forEach(step => step.classList.remove('active'));
    steps[stepName].classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// フォーム送信処理
document.getElementById('input-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('name').value.trim();
    const birthDate = document.getElementById('birth-date').value;
    
    if (!name || !birthDate) {
        alert('名前と生年月日を入力してください');
        return;
    }
    
    // ローディング画面に遷移
    showStep('loading');
    animateProgressSteps();
    
    try {
        // バックエンドに分析リクエストを送信
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                birth_date: birthDate
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'エラーが発生しました');
        }
        
        const result = await response.json();
        
        // 結果を表示
        displayResult(result);
        showStep('result');
        
    } catch (error) {
        console.error('Error:', error);
        alert(`エラーが発生しました: ${error.message}`);
        showStep('welcome');
    }
});

// プログレスステップのアニメーション
function animateProgressSteps() {
    const progressSteps = document.querySelectorAll('.progress-step');
    let currentStep = 0;
    
    const interval = setInterval(() => {
        if (currentStep < progressSteps.length) {
            progressSteps[currentStep].classList.add('active');
            currentStep++;
        } else {
            clearInterval(interval);
        }
    }, 1000);
}

// 結果を表示
function displayResult(data) {
    const resultContent = document.getElementById('result-content');
    
    // Markdownライクなテキストを簡易的にHTMLに変換
    const formattedAnalysis = formatAnalysisText(data.analysis);
    
    const html = `
        <div class="analysis-result">
            ${formattedAnalysis}
        </div>
        
        <div class="profile-summary">
            <h2>📊 プロファイル概要</h2>
            <div class="profile-grid">
                <div class="profile-item">
                    <strong>数秘術プロファイル</strong>
                    <p>Life Path: ${data.numerology.life_path}</p>
                    <p>Destiny: ${data.numerology.destiny}</p>
                    <p>Soul: ${data.numerology.soul}</p>
                    <p>Personal Year: ${data.numerology.personal_year}</p>
                </div>
                <div class="profile-item">
                    <strong>九星気学プロファイル</strong>
                    <p>本命星: ${data.kigaku.honmei_name}</p>
                    <p>現在の座相: ${data.kigaku.position_name}</p>
                </div>
            </div>
        </div>
    `;
    
    resultContent.innerHTML = html;
}

// テキストを整形（簡易Markdown変換）
function formatAnalysisText(text) {
    if (!text) return '';
    
    // 【】で囲まれた部分を強調
    text = text.replace(/【([^】]+)】/g, '<h1>$1</h1>');
    
    // ◆を見出しに変換
    text = text.replace(/◆\s*([^\n]+)/g, '<h2>◆ $1</h2>');
    
    // ##を見出しに変換
    text = text.replace(/^## (.+)$/gm, '<h2>$1</h2>');
    
    // ###を小見出しに変換
    text = text.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    
    // ---を区切り線に変換
    text = text.replace(/^---$/gm, '<hr>');
    
    // 箇条書き（-）をリストに変換
    text = text.replace(/^- (.+)$/gm, '<li>$1</li>');
    text = text.replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>');
    
    // 強調（**）を太字に変換
    text = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    
    // 改行を<br>に変換（ただし見出しやリストの後は除く）
    text = text.replace(/\n/g, '<br>');
    text = text.replace(/<\/(h[123]|ul|li)><br>/g, '</$1>');
    text = text.replace(/<br><(h[123]|ul)/g, '<$1');
    
    return text;
}

// 再スタートボタン
document.getElementById('btn-restart').addEventListener('click', () => {
    document.getElementById('input-form').reset();
    showStep('welcome');
});

// ページ読み込み時
document.addEventListener('DOMContentLoaded', () => {
    console.log('Hybrid Life Strategist App loaded');
});
