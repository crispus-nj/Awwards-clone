const sidebar = document.querySelector('.sidebar')
document.getElementById('sidebar_btn').addEventListener('click', ()=> {
  console.log('clicked')
  sidebar.style.display = "block";
})