import { Container, Flex } from "@chakra-ui/react";
import { TodoList } from "./components/Todo/TodoList/TodoList.tsx";
import { TodoForm } from "./components/Todo/TodoForm/TodoForm.tsx";
import { useTodos } from "./components/Todo/useTodos.ts";
import { useEffect } from "react";

export const App = () => {
  const { todos, fetchTodos, createTodo, deleteTodo, patchTodo, toggleTodo } =
    useTodos();

  useEffect(() => {
    void fetchTodos();
  }, []);

  return (
    <Container maxWidth={"100%"} p={4}>
      <Flex gap={8}>
        <TodoForm createTodo={createTodo} />
        <TodoList
          todos={todos}
          deleteTodo={deleteTodo}
          patchTodo={patchTodo}
          toggleTodo={toggleTodo}
        />
      </Flex>
    </Container>
  );
};
