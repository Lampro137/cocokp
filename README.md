# 克苏鲁的呼唤 - KP智能助手部署指南

这个KP智能助手网页是一个包含AI交互功能的网站，可以部署到多种云平台。下面提供几种常用的部署方案。

## 部署选项概览

### 1. 使用Vercel一键部署（推荐）
Vercel是一个支持一键部署静态网站的平台，非常适合部署纯HTML/CSS/JS的项目。

### 2. 使用Netlify一键部署
Netlify也是一个流行的静态网站托管平台，同样支持一键部署。

### 3. 使用GitHub Pages部署
如果您已经将代码托管在GitHub上，可以使用GitHub Pages功能部署网站。

---

## 详细部署步骤

### 方法一：使用Vercel部署

1. **准备工作**
   - 确保您的项目中包含 `coc_kp_agent.html`、`wsw.py` 和 `vercel.json` 文件（本项目已包含）
   - 注册一个 [Vercel](https://vercel.com/) 账号

2. **部署步骤**
   
   **通过Vercel官网部署：**
   1. 访问 [Vercel官网](https://vercel.com/dashboard)
   2. 点击右上角的 "Add New" -> "Project"
   3. 选择 "Import Git Repository" 或 "Upload"
   4. 如果选择上传文件：
      - 点击 "Upload" 按钮
      - 选择并上传 `coc_kp_agent.html`、`wsw.py` 和 `vercel.json` 文件
      - 点击 "Deploy"
   5. 等待部署完成，Vercel会为您提供一个可访问的URL

   **通过命令行部署：**
   1. 安装Vercel CLI：
      ```bash
      npm install -g vercel
      ```
   2. 在项目目录中运行：
      ```bash
      vercel
      ```
   3. 按照提示完成部署流程

### 方法二：使用Netlify部署

1. **准备工作**
   - 确保您的项目中包含 `coc_kp_agent.html` 和 `wsw.py` 文件
   - 注册一个 [Netlify](https://www.netlify.com/) 账号

2. **部署步骤**
   1. 访问 [Netlify官网](https://app.netlify.com/)
   2. 点击 "Add new site" -> "Deploy manually"
   3. 拖拽 `coc_kp_agent.html` 和 `wsw.py` 文件到上传区域
   4. 等待部署完成，Netlify会为您提供一个可访问的URL

### 方法三：使用GitHub Pages部署

1. **准备工作**
   - 在GitHub上创建一个新的仓库
   - 将您的项目代码（包括 `coc_kp_agent.html` 和 `wsw.py`）上传到这个仓库

2. **部署步骤**
   1. 进入您的GitHub仓库页面
   2. 点击 "Settings" -> "Pages"
   3. 在 "Source" 部分，选择 "main" 分支，然后选择 "/ (root)"
   4. 点击 "Save"
   5. 等待几分钟，GitHub Pages会为您构建并部署网站
   6. 部署完成后，您可以在页面顶部看到部署后的URL

---

## 自定义域名配置

如果您有自己的域名，可以在各个平台的设置中配置自定义域名：

- **Vercel**: 在项目设置的 "Domains" 部分添加您的域名
- **Netlify**: 在项目设置的 "Domain settings" 部分添加您的域名
- **GitHub Pages**: 在仓库设置的 "Pages" 部分添加自定义域名

---

## 技术说明

- 前端使用HTML5、CSS3 (Tailwind CSS)和JavaScript
- 使用了Font Awesome图标和Chart.js
- 包含AI交互功能，通过wsw.py提供后端服务
- 支持响应式设计，兼容移动端和桌面端

---

## 常见问题

**Q: 部署后网页无法正常显示怎么办？**
A: 检查浏览器控制台是否有错误信息，确保所有资源（CSS、JavaScript、图标）都能正确加载。

**Q: 如何更新已部署的网站？**
A: 根据您选择的部署平台，重新上传更新后的文件或推送代码到仓库，平台会自动重新部署。

**Q: 部署后访问速度慢怎么办？**
A: 可以考虑压缩HTML、CSS和JavaScript文件，减少文件大小以提高加载速度。