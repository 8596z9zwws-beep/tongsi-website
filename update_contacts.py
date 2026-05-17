#!/usr/bin/env python3
"""批量更新同思网站所有HTML页面的联系方式"""
import os

BASE = "/Users/liujie/.openclaw/workspace/tongsi-website"

INFO = {
    "zh": {
        "address": "云南省昆明市西山区融城优郡B座写字楼6楼606",
        "phone": "+86 159 2516 5428",
        "email": "14989056@qq.com",
        "wechat": "滇池呈海",
        "footer_title": "联系方式",
        "footer_wechat": "微信：滇池呈海"
    },
    "vi": {
        "address": "Tầng 6, Phòng 606, Tòa nhà B, Rongcheng Youjun, Quận Xishan, Côn Minh, Vân Nam, Trung Quốc",
        "phone": "+86 159 2516 5428",
        "email": "14989056@qq.com",
        "wechat": "滇池呈海",
        "footer_title": "Thông tin liên hệ",
        "footer_wechat": "WeChat: 滇池呈海"
    },
    "en": {
        "address": "Room 606, 6th Floor, Block B, Rongcheng Youjun Office Building, Xishan District, Kunming, Yunnan, China",
        "phone": "+86 159 2516 5428",
        "email": "14989056@qq.com",
        "wechat": "滇池呈海",
        "footer_title": "Contact Info",
        "footer_wechat": "WeChat: 滇池呈海"
    }
}

def process_file(filepath, lang):
    info = INFO[lang]
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. 替换中文首页联系段落的占位符
    if lang == "zh" and "云南省昆明市（待补充）" in content:
        content = content.replace("云南省昆明市（待补充）", info['address'])
        content = content.replace(
            '<div class="contact-icon">📞</div>\n          <div class="contact-text">\n            <h4>联系电话</h4>\n            <p>（待补充）</p>',
            '<div class="contact-icon">📞</div>\n          <div class="contact-text">\n            <h4>联系电话</h4>\n            <p>' + info['phone'] + '</p>'
        )
        content = content.replace(
            '<div class="contact-icon">✉️</div>\n          <div class="contact-text">\n            <h4>电子邮箱</h4>\n            <p>（待补充）</p>',
            '<div class="contact-icon">✉️</div>\n          <div class="contact-text">\n            <h4>电子邮箱</h4>\n            <p>' + info['email'] + '</p>'
        )
        content = content.replace(
            '<div class="contact-icon">💬</div>\n          <div class="contact-text">\n            <h4>微信</h4>\n            <p>（待补充）</p>',
            '<div class="contact-icon">💬</div>\n          <div class="contact-text">\n            <h4>微信</h4>\n            <p>' + info['wechat'] + '</p>'
        )
        content = content.replace(
            '<p style="font-size:13px; margin-top:8px;">云南省昆明市</p>',
            '<p style="font-size:13px; margin-top:8px;">' + info['address'] + '</p>'
        )
        print(f"  ✅ 更新联系段落: {filepath}")

    # 2. 替换越南语首页联系段落
    if lang == "vi" and "Côn Minh（待补充）" in content:
        content = content.replace("Côn Minh（待补充）", info['address'])
        # 类似替换...
        print(f"  ✅ 更新联系段落: {filepath}")

    # 3. 替换英文首页联系段落
    if lang == "en" and "Kunming, Yunnan (TBD)" in content:
        content = content.replace("Kunming, Yunnan (TBD)", info['address'])
        print(f"  ✅ 更新联系段落: {filepath}")

    # 4. 给所有页面的 footer 添加联系方式（如果还没有的话）
    if "footer-section" not in content or ("📞" not in content and "Contact" not in content.split("footer-section")[0][-200:] if "footer-section" in content else True):
        # 检查 footer-bottom 前是否有联系方式区块
        if "footer-bottom" in content and info['footer_title'] not in content:
            footer_block = f'''
      <div class="footer-section">
        <h3>{info['footer_title']}</h3>
        <p>📞 {info['phone']}</p>
        <p>📧 {info['email']}</p>
        <p>📍 {info['address']}</p>
        <p>📱 {info['footer_wechat']}</p>
      </div>'''
            content = content.replace(
                '<div class="footer-bottom">',
                footer_block + '\n    <div class="footer-bottom">'
            )
            print(f"  ✅ 添加页脚联系方式: {filepath}")

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 已保存: {filepath}")
    else:
        print(f"  ⊙ 无需修改: {filepath}")

# 执行
for lang in ["zh", "vi", "en"]:
    lang_dir = os.path.join(BASE, lang)
    if not os.path.exists(lang_dir):
        continue
    for fname in os.listdir(lang_dir):
        if fname.endswith(".html"):
            fpath = os.path.join(lang_dir, fname)
            process_file(fpath, lang)

print("\n✅ 全部处理完成！")
