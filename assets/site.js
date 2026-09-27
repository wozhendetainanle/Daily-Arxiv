const dateSelect = document.querySelector('#date-select');
const search = document.querySelector('#search');
const topics = document.querySelector('#topics');
const cards = document.querySelector('#cards');
const count = document.querySelector('#count');
const empty = document.querySelector('#empty');
const reportLink = document.querySelector('#report-link');
let archive = [];
let selectedTopic = '全部';

function el(name, className, text) {
  const node = document.createElement(name);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function link(label, href, className) {
  const a = el('a', className, label);
  a.href = href;
  if (href.startsWith('https://')) {
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
  }
  return a;
}

function renderTopics(papers) {
  const names = ['全部', ...new Set(papers.map(paper => paper.topic))];
  if (!names.includes(selectedTopic)) selectedTopic = '全部';
  topics.replaceChildren(...names.map(name => {
    const button = el('button', name === selectedTopic ? 'active' : '', name);
    button.type = 'button';
    button.addEventListener('click', () => { selectedTopic = name; render(); });
    return button;
  }));
}

function card(paper, date) {
  const article = el('article', 'card');
  const thumb = el('div', paper.image ? 'thumb' : 'thumb fallback');
  if (paper.image) {
    const image = el('img');
    image.src = paper.image;
    image.alt = `${paper.title} 的论文或项目配图`;
    image.loading = 'lazy';
    thumb.append(image);
    if (paper.imageSource) thumb.title = `图片来源：${paper.imageSource}`;
  }
  thumb.append(el('span', 'topic-label', paper.topic));
  article.append(thumb);
  const body = el('div', 'card-body');
  const meta = el('div', 'meta', paper.venue || `arXiv ${date} · ${paper.category.split(';')[0].trim()}`);
  meta.append(el('span', 'rank', `#${paper.rank}`));
  body.append(meta);
  const heading = el('h2');
  heading.append(link(paper.title, paper.links.Paper));
  body.append(heading, el('p', 'authors', paper.authors));
  const links = el('div', 'card-links');
  Object.entries(paper.links).forEach(([label, href]) => links.append(link(label, href)));
  body.append(links);
  article.append(body);
  return article;
}

function render() {
  const day = archive.find(item => item.date === dateSelect.value) || archive[0];
  if (!day) return;
  renderTopics(day.papers);
  reportLink.href = day.report;
  const query = search.value.trim().toLocaleLowerCase();
  const shown = day.papers.filter(paper =>
    (selectedTopic === '全部' || paper.topic === selectedTopic) &&
    (!query || `${paper.title} ${paper.authors} ${paper.category}`.toLocaleLowerCase().includes(query))
  );
  cards.replaceChildren(...shown.map(paper => card(paper, day.date)));
  count.textContent = `${shown.length} / ${day.papers.length} 篇`;
  empty.hidden = shown.length > 0;
  empty.textContent = day.papers.length ? '这个筛选下没有论文。' : '这一天没有新增论文；可阅读完整中文日报。';
}

fetch('data/papers.json')
  .then(response => { if (!response.ok) throw new Error('无法读取论文数据'); return response.json(); })
  .then(data => {
    archive = data.dates;
    dateSelect.replaceChildren(...archive.map(day => {
      const option = el('option', '', `${day.date}${day.papers.length ? '' : ' · 无新增'}`);
      option.value = day.date;
      return option;
    }));
    const requested = new URLSearchParams(location.search).get('date');
    dateSelect.value = archive.some(day => day.date === requested)
      ? requested : (archive.find(day => day.papers.length)?.date || archive[0].date);
    dateSelect.addEventListener('change', () => { selectedTopic = '全部'; render(); });
    search.addEventListener('input', render);
    render();
  })
  .catch(error => {
    empty.hidden = false;
    empty.textContent = `${error.message}。请从网页服务器或 GitHub Pages 打开此页面。`;
  });
