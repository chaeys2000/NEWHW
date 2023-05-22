/*JS 부분*/

/* DOM 접근 및 변수 선언 */
const todoForm = document.getElementById("todo-form"); // 투두입력 받는 form태그
const todoList = document.getElementById("todo-list"); // 투두항목 나열되는 ul태그
const submitBtn = document.querySelector(".submitBtn"); // 투두항목 제출하는 버튼
const content = document.querySelector("#content");
let todoArr = [];
const key = "TODOs";

/*Event Handler*/

/*TodoForm 제출*/
function submitAddTodo(event) {
  event.preventDefault(); //새로고침 방지
  const todoObj = {
    text: content.value,
    id: Date.now()
  };
  todoArr.push(todoObj); //입력되는 todoList 하나 todoArr 배열에 push
  saveTodos();
  paintTodo(todoObj); //입력되는 todoList 하나 Paint
  content.value = "";
}
todoForm.addEventListener("submit", submitAddTodo);

/*TodoList 삭제*/
function deleteTodo(event) {
  const li = event.target.parentElement;
  li.remove();
  const id = parseInt(li.id);
  todoArr = todoArr.filter((todo) => todo.id !== id); //todoArr에서 삭제된 li.id랑 같은 id 가진 객체 삭제
  saveTodos(); //삭제된 todoArr LocalStorage에 저장
}

/*TodoList 렌더링*/
function paintTodo(todo) {
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = todo.text;
  const button = document.createElement("button");
  button.innerText = "X";
  button.addEventListener("click", deleteTodo);
  const todoList = document.getElementById("todo-list");
  todoList.appendChild(li);
  li.appendChild(span);
  li.appendChild(button);
  li.id = todo.id;
}

/*TodoList localStorage에 저장*/

function saveTodos() {
  localStorage.setItem(key, JSON.stringify(todoArr)); //localStorage에 저장할 때는 꼭 JSON.stringify써서 JSON 문자열 형태로 저장할 것
}

/* 페이지 로드 시 localStorage 데이터 불러오기 */
function loadTodos() {
  const savedTodos = localStorage.getItem(key);
  if (savedTodos) {
    todoArr = JSON.parse(savedTodos);
    todoArr.forEach((todo) => paintTodo(todo));
  }
}

loadTodos();