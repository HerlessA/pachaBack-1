var botonGuardar = document.getElementById("guardar-btn");
const userForm = document.querySelector("#userForm");

let users = [];
let editing = false;
let userId = null;
const BASE_URL = "http://127.0.0.1:5000";

window.addEventListener("DOMContentLoaded", async () => {
  const response = await fetch(`${BASE_URL}/api/obtenerUsuarios`);
  const data = await response.json();
  users = data;
  console.log(users);
  renderUser(users);
});
userForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = userForm["name"].value;
  const password = userForm["password"].value;
  const email = userForm["email"].value;
  if (botonGuardar.textContent == "Guardar") {
    // send user to backend

    const response = await fetch(`${BASE_URL}/api/crearUsuario`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        email: email,
        password: password,
      }),
    });

    const data = await response.json();
    users.push(data);
    renderUser(users);

    location.reload();
  } else {
    const response = await fetch(
      `${BASE_URL}/api/actualizarUsuario/${userId}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
          email: email,
          password: password,
        }),
      }
    );

    botonGuardar.textContent = "Guardar";
  }
  userForm.reset();
  location.reload();
});

function renderUser(users) {
  const userList = document.querySelector("#userList");
  userList.innerHTML = "";
  users.forEach((user) => {
    const userItem = document.createElement("li");
    userItem.classList = "list-group-item list-group-item-dark my-2";
    userItem.innerHTML = `
        <header class="d-flex justify-content-between align-items-center">
          <h3>${user.name}</h3>
          <div>
            <button data-id="${user.id}" class="btn-delete btn btn-danger btn-sm">Delete</button>
            <button data-id="${user.id}" class="btn-edit btn btn-secondary btn-sm">Edit</button>
          </div>
        </header>
        <p>${user.email}</p>
        <p class="text-truncate">${user.password}</p>
    `;

    // Handle delete button
    const btnDelete = userItem.querySelector(".btn-delete");

    btnDelete.addEventListener("click", async (e) => {
      const response = await fetch(
        `${BASE_URL}/api/eliminarUsuario/${user.id}`,
        {
          method: "DELETE",
        }
      );

      const data = await response.json();
      users = users.filter((user) => user.id !== data.id);
      renderUser(users);
      location.reload();
    });

    userList.appendChild(userItem);

    // Handle edit button
    const btnEdit = userItem.querySelector(".btn-edit");

    btnEdit.addEventListener("click", async (e) => {
      const response = await fetch(
        `${BASE_URL}/api/encontrarUsuario/${user.id}`,
        { method: "GET" }
      );
      console.log("response", response);
      const data = await response.json();
      console.log("data", data);

      userForm["name"].value = data.name;
      userForm["email"].value = data.email;
      userForm["password"].value = data.password;

      userId = user.id;

      botonGuardar.textContent = "Actualizar";
    });
  });
}
