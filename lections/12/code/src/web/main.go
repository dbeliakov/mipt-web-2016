package main

import (
	"html/template"
	"net/http"
)

func IndexHandler(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name")
	if len(name) == 0 {
		name = "Аноним"
	}
	t, err := template.ParseFiles("templates/index.tpl")
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
	}
	t.Execute(w, map[string]string{"Name": name})
}

func main() {
	http.HandleFunc("/", IndexHandler)
	http.ListenAndServe(":8080", nil)
}
