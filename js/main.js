// 云南同思商贸网站 - 主脚本

// 移动端菜单切换
function toggleMenu() {
  const menu = document.querySelector('.nav-menu');
  menu.classList.toggle('active');
}

// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href !== '#') {
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    }
  });
});

// 表单提交处理（如果使用 EmailJS）
// 需要先引入 EmailJS SDK: <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
/*
function sendEmail(e) {
  e.preventDefault();
  emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', e.target)
    .then(() => {
      alert('询价已提交，我们将尽快联系您！');
      e.target.reset();
    }, (error) => {
      alert('提交失败，请稍后重试或直接联系我们。');
      console.error(error);
    });
}
*/

// 导航栏滚动效果
let lastScroll = 0;
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  const currentScroll = window.pageYOffset;

  if (currentScroll > 100) {
    navbar.style.boxShadow = '0 2px 20px rgba(26,58,92,0.15)';
  } else {
    navbar.style.boxShadow = '0 2px 12px rgba(26,58,92,0.1)';
  }

  lastScroll = currentScroll;
});

// 页面加载完成
document.addEventListener('DOMContentLoaded', () => {
  // 移除加载状态（如果有）
  document.body.classList.add('loaded');
});
