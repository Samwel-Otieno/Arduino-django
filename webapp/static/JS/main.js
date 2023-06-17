// display the data only on request
const buttons=document.getElementById('bang');
const data=document.getElementById('show_data');
const toggle_visibility=() =>{
    if (data.classList.contains('hidden')) {
        data.classList.remove('hidden');
        buttons.innerText='Hide data';
      } else {
        data.classList.add('hidden');
        buttons.innerText='Show data';

      }
};

buttons.onclick=toggle_visibility;