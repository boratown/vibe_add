const STORAGE_KEY = 'todo-app-items-v1';
const list = document.getElementById('todo-list');
const form = document.getElementById('todo-form');
const input = document.getElementById('todo-input');
const messageEl = document.getElementById('message');
const countEl = document.getElementById('todo-count');
const filterButtons = Array.from(document.querySelectorAll('.filter-btn'));
let todos = [];
let currentFilter = 'all';

function loadTodosFromStorage() {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    todos = stored ? JSON.parse(stored) : [];
  } catch (error) {
    todos = [];
  }
}

function saveTodos() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
}

function getVisibleTodos() {
  if (currentFilter === 'completed') return todos.filter((item) => item.completed);
  if (currentFilter === 'active') return todos.filter((item) => !item.completed);
  return todos;
}

function updateSummary() {
  const remaining = todos.filter((item) => !item.completed).length;
  countEl.textContent = `남은 할 일 ${remaining}개`;
}

function renderTodos() {
  const visibleTodos = getVisibleTodos();
  messageEl.textContent = '';
  if (!todos.length) {
    list.innerHTML = '<li class="empty">아직 할 일이 없어요. 첫 할 일을 추가해 보세요.</li>';
    updateSummary();
    return;
  }

  if (!visibleTodos.length) {
    list.innerHTML = '<li class="empty">이 필터에 해당하는 할 일이 없어요.</li>';
    updateSummary();
    return;
  }

  list.innerHTML = visibleTodos.map((item) => `
    <li>
      <div class="todo-left">
        <input type="checkbox" ${item.completed ? 'checked' : ''} onchange="toggleTodo(${item.id})">
        <span class="todo-title ${item.completed ? 'completed' : ''}">${item.title}</span>
      </div>
      <div class="actions">
        <button class="toggle-btn" type="button" onclick="toggleTodo(${item.id})">${item.completed ? '복원' : '완료'}</button>
        <button class="delete-btn" type="button" onclick="deleteTodo(${item.id})">삭제</button>
      </div>
    </li>
  `).join('');
  updateSummary();
}

function setFilter(filter) {
  currentFilter = filter;
  filterButtons.forEach((button) => {
    button.classList.toggle('active', button.dataset.filter === filter);
  });
  renderTodos();
}

function addTodo(title) {
  const trimmedTitle = title.trim();
  if (!trimmedTitle) {
    messageEl.textContent = '할 일을 입력해 주세요.';
    return;
  }
  todos.push({ id: Date.now(), title: trimmedTitle, completed: false });
  saveTodos();
  renderTodos();
  input.value = '';
}

function toggleTodo(id) {
  todos = todos.map((item) => item.id === id ? { ...item, completed: !item.completed } : item);
  saveTodos();
  renderTodos();
}

function deleteTodo(id) {
  if (!window.confirm('정말 삭제하시겠어요?')) return;
  todos = todos.filter((item) => item.id !== id);
  saveTodos();
  renderTodos();
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  addTodo(input.value);
});

filterButtons.forEach((button) => {
  button.addEventListener('click', () => setFilter(button.dataset.filter));
});

window.toggleTodo = toggleTodo;
window.deleteTodo = deleteTodo;

loadTodosFromStorage();
renderTodos();
