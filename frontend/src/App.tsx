import { Button, Container, SimpleGrid } from "@chakra-ui/react";
import { TodoList } from "./components/Todo/TodoList/TodoList.tsx";
import { TodoForm } from "./components/Todo/TodoForm/TodoForm.tsx";
import { useTodos } from "./components/Todo/useTodos.ts";
import { useEffect, useState } from "react";

export const App = () => {
  const { todos, fetchTodos, submitTodo, deleteTodo } = useTodos();
  const [isFormVisible, setIsFormVisible] = useState<boolean>(false);

  const closeForm = () => {
    setIsFormVisible(false);
  };

  const openForm = () => {
    setIsFormVisible(true);
  };

  useEffect(() => {
    void fetchTodos();
  }, []);

  return (
    <Container maxWidth={"100%"} p={4}>
      <Button onClick={openForm}>Открыть форму</Button>
      <TodoForm
        isVisible={isFormVisible}
        closeForm={closeForm}
        submitTodo={submitTodo}
      />
      <SimpleGrid columns={3} spacing={5}>
        <TodoList
          todos={todos.filter((todo) => todo.status === "waiting")}
          heading={"Задачи в ожидании"}
          deleteTodo={deleteTodo}
        />
        <TodoList
          todos={todos.filter((todo) => todo.status === "in_progress")}
          heading={"Текущие задачи"}
          deleteTodo={deleteTodo}
        />
        <TodoList
          todos={todos.filter((todo) => todo.status === "done")}
          heading={"Выполненные задачи"}
          deleteTodo={deleteTodo}
        />
      </SimpleGrid>
    </Container>
  );
};
