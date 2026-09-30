const fileInput = document.querySelector('#file-input');
const dropZone = document.querySelector('#drop-zone');
const progressWrap = document.querySelector('#progress-wrap');
const progressBar = document.querySelector('#progress-bar');
const uploadStatus = document.querySelector('#upload-status');
const toast = document.querySelector('#toast');
const result = document.querySelector('#result');
const resultContent = document.querySelector('#result-content');
const resultLoading = document.querySelector('#result-loading');
const loadingTitle = document.querySelector('#loading-title');
const loadingSubtitle = document.querySelector('#loading-subtitle');
const titles = {
  summarize: 'Document Summary',
  practice: 'Practice Questions',
  mcq: 'Multiple Choice Questions',
  explain: 'Topic Explanation',
};
const loadingSteps = {
  summarize: [
    'Reading your document…',
    'Finding the most important ideas…',
    'Organizing short and detailed summaries…',
    'Formatting the final result…',
  ],
  practice: [
    'Reviewing the study material…',
    'Creating short and long questions…',
    'Adding viva questions and difficulty labels…',
    'Polishing the final list…',
  ],
  mcq: [
    'Analyzing your document…',
    'Writing 10 balanced questions…',
    'Checking options and explanations…',
    'Preparing your interactive quiz…',
  ],
  explain: [
    'Understanding your topic…',
    'Finding supporting details in the document…',
    'Creating a simple explanation…',
  ],
};
let plainResult = '';
let busy = false;
let uploading = false;
let loadingTimer;
let activeActionButton;

function notify(message, error = false) {
  toast.textContent = message;
  toast.className = `toast show${error ? ' error' : ''}`;
  clearTimeout(notify.timer);
  notify.timer = setTimeout(() => toast.className = 'toast', 3200);
}

function errorMessage(payload, fallback) {
  return payload?.detail || fallback;
}

function setActionsEnabled(enabled) {
  document.querySelectorAll('.action-card').forEach((button) => button.disabled = !enabled);
  document.querySelector('#topic-input').disabled = !enabled;
  document.querySelector('#explain-form button').disabled = !enabled;
}

function updateDocument(info) {
  document.querySelector('#empty-document').hidden = true;
  document.querySelector('#document-details').hidden = false;
  document.querySelector('#filename').textContent = info.filename;
  document.querySelector('#filetype').textContent = info.filetype;
  document.querySelector('#word-count').textContent = info.word_count.toLocaleString();
  document.querySelector('#character-count').textContent = info.character_count.toLocaleString();
  document.querySelector('#uploaded-at').textContent = new Date(info.uploaded_at).toLocaleString();

  const status = document.querySelector('#document-status');
  status.textContent = 'Ready';
  status.style.color = '#16803c';
  setActionsEnabled(true);
  plainResult = '';
  result.hidden = true;

  const card = document.querySelector('#document-info');
  card.classList.add('success-pulse');
  setTimeout(() => card.classList.remove('success-pulse'), 700);
}

function setUploading(isUploading, message = '') {
  uploading = isUploading;
  dropZone.classList.toggle('processing', isUploading);
  uploadStatus.hidden = !isUploading;
  uploadStatus.textContent = message;
}

function upload(file) {
  if (!file || uploading) return;
  const form = new FormData();
  form.append('file', file);
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/upload');
  setUploading(true, `Uploading ${file.name}…`);
  progressWrap.hidden = false;
  progressBar.style.width = '0%';
  xhr.upload.onprogress = (event) => {
    if (!event.lengthComputable) return;
    const percent = Math.round((event.loaded / event.total) * 100);
    progressBar.style.width = `${percent}%`;
    uploadStatus.textContent = percent === 100 ? 'Extracting document text…' : `Uploading ${file.name}… ${percent}%`;
  };
  xhr.onload = () => {
    progressWrap.hidden = true;
    setUploading(false);
    let payload = {};
    try { payload = JSON.parse(xhr.responseText); } catch {}
    if (xhr.status >= 200 && xhr.status < 300) {
      updateDocument(payload.document);
      notify(payload.message);
    } else {
      notify(errorMessage(payload, 'Upload failed.'), true);
    }
    fileInput.value = '';
  };
  xhr.onerror = () => {
    progressWrap.hidden = true;
    setUploading(false);
    notify('Network error. Please try again.', true);
  };
  xhr.send(form);
}

fileInput?.addEventListener('change', (event) => upload(event.target.files[0]));
['dragenter', 'dragover'].forEach((name) => dropZone?.addEventListener(name, (event) => {
  event.preventDefault();
  if (!uploading) dropZone.classList.add('dragging');
}));
['dragleave', 'drop'].forEach((name) => dropZone?.addEventListener(name, (event) => {
  event.preventDefault();
  dropZone.classList.remove('dragging');
}));
dropZone?.addEventListener('drop', (event) => upload(event.dataTransfer.files[0]));

function mcqToText(questions) {
  return questions.map((item) => {
    const options = Object.entries(item.options).map(([letter, option]) => `${letter}. ${option}`).join('\n');
    return `${item.number}. ${item.question}\n${options}\nCorrect Answer: ${item.correct_answer}\nExplanation: ${item.explanation}`;
  }).join('\n\n');
}

function renderMCQs(questions) {
  let answered = 0;
  let score = 0;
  const scoreBoard = document.createElement('div');
  scoreBoard.className = 'mcq-score';
  const scoreText = document.createElement('strong');
  const scoreMeta = document.createElement('span');
  const retake = document.createElement('button');
  retake.type = 'button';
  retake.className = 'mcq-retake';
  retake.textContent = 'Retake quiz';
  retake.hidden = true;
  const progressTrack = document.createElement('div');
  progressTrack.className = 'mcq-progress';
  const progressFill = document.createElement('span');
  progressTrack.appendChild(progressFill);
  const scoreHeader = document.createElement('div');
  scoreHeader.className = 'mcq-score-header';
  scoreHeader.append(scoreText, retake);
  scoreBoard.append(scoreHeader, scoreMeta, progressTrack);
  const cards = document.createElement('div');
  cards.className = 'mcq-list';

  const updateScore = () => {
    const complete = answered === questions.length;
    const percentage = questions.length ? Math.round((score / questions.length) * 100) : 0;
    scoreBoard.classList.toggle('complete', complete);
    scoreText.textContent = complete ? `Final marks: ${score} / ${questions.length}` : `Question progress`;
    scoreMeta.textContent = complete
      ? `You scored ${percentage}%. Review the highlighted answers and explanations below.`
      : `${answered} of ${questions.length} answered · Current score ${score}`;
    progressFill.style.width = `${(answered / questions.length) * 100}%`;
    retake.hidden = !complete;
  };

  retake.addEventListener('click', () => {
    renderMCQs(questions);
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  questions.forEach((item) => {
    const card = document.createElement('article');
    card.className = 'mcq-card';
    const cardTop = document.createElement('div');
    cardTop.className = 'mcq-card-top';
    const questionNumber = document.createElement('span');
    questionNumber.className = 'question-number';
    questionNumber.textContent = `Question ${item.number}`;
    const answerStatus = document.createElement('span');
    answerStatus.className = 'answer-status';
    cardTop.append(questionNumber, answerStatus);
    const question = document.createElement('h3');
    question.textContent = item.question;
    const options = document.createElement('div');
    options.className = 'mcq-options';
    const explanation = document.createElement('div');
    explanation.className = 'mcq-explanation';
    explanation.hidden = true;
    const explanationLabel = document.createElement('strong');
    explanationLabel.textContent = 'Explanation';
    const explanationText = document.createElement('p');
    explanationText.textContent = item.explanation;
    explanation.append(explanationLabel, explanationText);

    Object.entries(item.options).forEach(([letter, text]) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'mcq-option';
      button.dataset.letter = letter;
      const optionLetter = document.createElement('span');
      optionLetter.className = 'option-letter';
      optionLetter.textContent = letter;
      const optionText = document.createElement('span');
      optionText.className = 'option-text';
      optionText.textContent = text;
      const optionIcon = document.createElement('span');
      optionIcon.className = 'option-icon';
      button.append(optionLetter, optionText, optionIcon);
      button.addEventListener('click', () => {
        if (card.dataset.answered === 'true') return;
        card.dataset.answered = 'true';
        answered += 1;
        options.querySelectorAll('button').forEach((option) => option.disabled = true);
        const correctOption = options.querySelector(`[data-letter="${item.correct_answer}"]`);
        correctOption?.classList.add('correct');
        if (correctOption) correctOption.querySelector('.option-icon').textContent = '✓';
        if (letter === item.correct_answer) {
          score += 1;
          button.classList.add('selected');
          card.classList.add('correct-card');
          answerStatus.textContent = 'Correct';
          answerStatus.classList.add('correct-label');
        } else {
          button.classList.add('incorrect', 'selected');
          button.querySelector('.option-icon').textContent = '✕';
          card.classList.add('incorrect-card');
          answerStatus.textContent = 'Incorrect';
          answerStatus.classList.add('incorrect-label');
        }
        explanation.hidden = false;
        updateScore();
      });
      options.appendChild(button);
    });

    card.append(cardTop, question, options, explanation);
    cards.appendChild(card);
  });

  updateScore();
  resultContent.replaceChildren(scoreBoard, cards);
}

function startLoading(action) {
  let step = 0;
  const steps = loadingSteps[action] || loadingSteps.summarize;
  loadingTitle.textContent = `Generating ${titles[action].toLowerCase()}`;
  loadingSubtitle.textContent = steps[step];
  clearInterval(loadingTimer);
  loadingTimer = setInterval(() => {
    step = Math.min(step + 1, steps.length - 1);
    loadingSubtitle.textContent = steps[step];
  }, 1800);
}

function stopLoading() {
  clearInterval(loadingTimer);
  resultLoading.hidden = true;
  document.body.classList.remove('api-busy');
  activeActionButton?.classList.remove('is-loading');
  activeActionButton?.removeAttribute('aria-busy');
}

function renderError(message, retry) {
  const error = document.createElement('div');
  error.className = 'error-panel';
  const icon = document.createElement('span');
  icon.textContent = '!';
  const text = document.createElement('div');
  const title = document.createElement('strong');
  title.textContent = 'Something went wrong';
  const detail = document.createElement('p');
  detail.textContent = message;
  const retryButton = document.createElement('button');
  retryButton.type = 'button';
  retryButton.className = 'secondary-button';
  retryButton.textContent = 'Try again';
  retryButton.addEventListener('click', retry);
  text.append(title, detail);
  error.append(icon, text, retryButton);
  resultContent.replaceChildren(error);
}

async function runAction(action, body) {
  if (busy) return;
  busy = true;
  result.hidden = false;
  resultContent.replaceChildren();
  resultLoading.hidden = false;
  document.querySelector('#result-title').textContent = titles[action];
  result.scrollIntoView({ behavior: 'smooth', block: 'start' });
  document.body.classList.add('api-busy');
  activeActionButton = document.querySelector(`.action-card[data-action="${action}"]`);
  activeActionButton?.classList.add('is-loading');
  activeActionButton?.setAttribute('aria-busy', 'true');
  document.querySelectorAll('[data-action]').forEach((button) => button.disabled = true);
  startLoading(action);

  try {
    const response = await fetch(`/${action}`, {
      method: 'POST',
      headers: body ? { 'Content-Type': 'application/json' } : {},
      body: body ? JSON.stringify(body) : undefined,
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(errorMessage(payload, 'Request failed.'));
    if (action === 'mcq') {
      plainResult = mcqToText(payload.questions);
      renderMCQs(payload.questions);
      notify('Your 10-question quiz is ready.');
    } else {
      plainResult = payload.content;
      resultContent.innerHTML = payload.html;
      notify(`${titles[action]} generated.`);
    }
  } catch (error) {
    notify(error.message, true);
    renderError(error.message, () => runAction(action, body));
  } finally {
    busy = false;
    stopLoading();
    document.querySelectorAll('[data-action]').forEach((button) => button.disabled = false);
  }
}

document.querySelectorAll('.action-card[data-action]').forEach((button) => {
  button.addEventListener('click', () => runAction(button.dataset.action));
});
document.querySelectorAll('.nav-link[data-action]').forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    if (!document.querySelector('#topic-input').disabled) runAction(link.dataset.action);
  });
});
document.querySelector('[data-scroll]')?.addEventListener('click', (event) => {
  document.querySelector(`#${event.currentTarget.dataset.scroll}`).scrollIntoView({ behavior: 'smooth' });
});

const topicInput = document.querySelector('#topic-input');
topicInput?.addEventListener('input', () => {
  document.querySelector('#topic-counter').textContent = `${topicInput.value.length} / 500`;
});
document.querySelector('#explain-form')?.addEventListener('submit', (event) => {
  event.preventDefault();
  if (topicInput.reportValidity()) runAction('explain', { prompt: topicInput.value.trim() });
});
document.querySelector('#copy-button')?.addEventListener('click', async () => {
  await navigator.clipboard.writeText(plainResult);
  notify('Result copied.');
});
document.querySelector('#download-button')?.addEventListener('click', () => {
  const url = URL.createObjectURL(new Blob([plainResult], { type: 'text/plain' }));
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = 'study-assistant-result.txt';
  anchor.click();
  URL.revokeObjectURL(url);
});

const sidebar = document.querySelector('#sidebar');
const overlay = document.querySelector('#drawer-overlay');
const menu = document.querySelector('#menu-button');
function closeMenu() {
  sidebar.classList.remove('open');
  overlay.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
}
menu?.addEventListener('click', () => {
  sidebar.classList.toggle('open');
  overlay.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(sidebar.classList.contains('open')));
});
overlay?.addEventListener('click', closeMenu);
document.querySelectorAll('.nav-link').forEach((link) => link.addEventListener('click', closeMenu));

fetch('/document')
  .then((response) => response.json())
  .then((payload) => { if (payload.document) updateDocument(payload.document); })
  .catch(() => {});
