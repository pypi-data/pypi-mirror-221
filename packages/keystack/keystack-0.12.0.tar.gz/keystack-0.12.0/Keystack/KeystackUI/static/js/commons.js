async function getData(url, csrftoken, method) {
  /* url: /path/to/somewhere
     csrftoken: The django generated token
     method: GET | DELETE
  */

  console.log(`getData() Rx: url=${url} method=${method}`)

  try {
    // http://172.16.1.16:8000/GlobalVariables/getGlobalVariables
    // body: JSON.stringify({'filePath': filePath.value}),
    // application/x-www-form-urlencoded;
    const response = await fetch(url, {
      method: method,
      mode: 'same-origin',
      credentials: 'include',
      redirect: 'follow',
      headers: {
        "Accept": "application/json, text/plain, */*",
        "X-CSRFToken": csrftoken,
        'Access-Control-Allow-Origin': '*',
      }
    });

    const data = await response.json();

    console.log('getData() returning data: ' + data.file)
    return data;
  } catch (error) {
    console.log("getData() error: " + error)
  };
}

async function postData(url, csrftoken, method, jsonBody) {
  /* url: /path/to/somewhere
     csrftoken: The django generated token
     method: POST
     jsonBody: {'data': 'value'}
  */

  console.log(`postData() Rx: url=${url} method=${method}  jsonBody=${jsonBody}`)

  try {
    // http://172.16.1.16:8000/GlobalVariables/getGlobalVariables
    // body: JSON.stringify({'filePath': filePath.value}),
    // application/x-www-form-urlencoded;
    const response = await fetch(url, {
      method: method,
      mode: 'same-origin',
      credentials: 'include',
      redirect: 'follow',
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "X-CSRFToken": csrftoken,
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify(jsonBody),
    });

    const data = await response.json();

    return data;
  } catch (error) {
    console.log("postData() error: " + error)
  };
}


function sortTable(tableId, columnIndex) {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.querySelector(tableId);

  switching = true;
  /*Make a loop that will continue until
  no switching has been done:*/

  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;

    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;

      /*Get the two elements you want to compare,
      one from current row and one from the next:
      TD[1] == column index
      */
      x = rows[i].getElementsByTagName("TD")[columnIndex];
      y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
      //check if the two rows should switch place:
      if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
        //if so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
      }
    }

    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}

function search(searchInputId, tableId, columnIndex) {
  var input, filter, table, tr, td, i, txtValue;
  input = document.querySelector(searchInputId);
  filter = input.value.toUpperCase();
  table = document.querySelector(tableId);
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    // [2] is the Playbook Group column
    td = tr[i].getElementsByTagName("td")[columnIndex];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}