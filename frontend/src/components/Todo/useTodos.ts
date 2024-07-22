import {useState} from "react";
import {Todo, TTodoForm} from "./types/TodoTypes.ts";
import {useToast} from "@chakra-ui/react";

export const useTodos = () => {
  const toast = useToast();
  const [todos, setTodos] = useState<Todo[]>([]);

  const fetchTodos = async () => {
    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/tasks?user_id=0`,
      );
      const json = await response.json();
      setTodos(json.data);
    } catch (error) {
      const e = error as Error;
      toast({
        title: "Ошибка",
        description: e.message,
        status: "error",
      });
      console.error(error);
    }
  };

  const submitTodo = async (data: TTodoForm) => {
    try {
      const method = data.id ? "PUT" : "POST";
      await fetch(`${import.meta.env.VITE_API_URL}/task`, {
        method,
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({...data, user_id: 0}),
      });
      toast({
        description: `Задача ${data.task} добавлена`,
        status: "success",
      });
      await fetchTodos();
    } catch (error) {
      const e = error as Error;
      toast({
        title: "Ошибка",
        description: e.message,
        status: "error",
      });
      console.error(error);
    }
  };

  const deleteTodo = async (id: number) => {
    try {
      await fetch(`${import.meta.env.VITE_API_URL}/task/${id}`, {
        method: "DELETE",
      });
      await fetchTodos();
    } catch (error) {
      const e = error as Error;
      toast({
        title: "Ошибка",
        description: e.message,
        status: "error",
      });
      console.error(error);
    }
  };

  return {
    todos,
    fetchTodos,
    submitTodo,
    deleteTodo,
  };
};
