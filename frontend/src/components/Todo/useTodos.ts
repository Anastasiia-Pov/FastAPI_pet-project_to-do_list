import { useState } from "react";
import { Todo, TTodoForm } from "./types/TodoTypes.ts";

export const useTodos = () => {
  const [todos, setTodos] = useState<Todo[]>([
    { text: "kek", is_active: true },
    { text: "lol", is_active: false },
    { text: "validol", is_active: true },
  ]);

  const fetchTodos = async () => {
    try {
      //const response = await fetch("/api/todos");
      //const json = await response.json();
      //setTodos(json);
      //setTodos([]);
    } catch (error) {
      console.error(error);
    }
  };

  const createTodo = async (data: TTodoForm) => {
    try {
      //await fetch("api/todos", { method: "POST", body: JSON.stringify(data) });
      //await fetchTodos();
      setTodos((prevState) => [...prevState, data]);
      console.log(todos);
    } catch (error) {
      console.error(error);
    }
  };

  const patchTodo = async (data: string) => {
    try {
      await fetch("api/todos", {
        method: "PATCH",
        body: JSON.stringify({ data }),
      });
      await fetchTodos();
    } catch (error) {
      console.error(error);
    }
  };

  const toggleTodo = async (text: string) => {
    try {
      const newTodos = todos.map((todo) => {
        if (todo.text === text) {
          return { ...todo, is_active: !todo.is_active };
        }
        return todo;
      });
      setTodos(newTodos);
    } catch (error) {
      console.error(error);
    }
  };

  const deleteTodo = async (text: string) => {
    try {
      //await fetch(`api/todos/${text}`, { method: "DELETE" });
      setTodos((prevState) => prevState.filter((todo) => todo.text !== text));
    } catch (error) {
      console.error(error);
    }
  };

  return {
    todos,
    fetchTodos,
    createTodo,
    patchTodo,
    toggleTodo,
    deleteTodo,
  };
};
