document.addEventListener("DOMContentLoaded", function(){
  const form=document.querySelector("#reed-filter-form")
  if (form){
    form.querySelectorAll("select").forEach(select => {
      select.addEventListener("change", function() {
        form.submit()
      })
    })
  }
}) 
