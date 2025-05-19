document.addEventListener("DOMContentLoaded", function () {
    const filterForm = document.querySelector("#reed-filter-form");
    if (filterForm) {
      const selects = filterForm.querySelectorAll("select");
      selects.forEach(select => {
        select.addEventListener("change", function () {
          filterForm.submit();
        });
      });
    }
});