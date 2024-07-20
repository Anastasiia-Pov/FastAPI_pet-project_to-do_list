import {
  Card,
  CardBody,
  CardHeader,
  OrderedList,
  Text,
} from "@chakra-ui/react";
import { TodoItem } from "../TodoItem/TodoItem.tsx";
import { Todo } from "../types/TodoTypes.ts";

type TTodoList = {
  todos: Todo[];
  deleteTodo: (value: string) => Promise<void>;
  patchTodo: (value: string) => Promise<void>;
  toggleTodo: (value: string) => Promise<void>;
};

export const TodoList = ({ todos, ...rest }: TTodoList) => {
  return (
    <Card width="100%">
      <CardHeader>
        <Text fontSize={"xl"} fontWeight={"bold"}>
          Текущие задачи
        </Text>
      </CardHeader>
      <CardBody>
        {todos.length ? (
          <OrderedList display={"flex"} flexDirection={"column"} gap={4}>
            {todos.map((todo, index) => (
              <TodoItem key={index} todo={todo} {...rest} />
            ))}
          </OrderedList>
        ) : (
          <Text>Нет задач</Text>
        )}
      </CardBody>
    </Card>
  );
};
