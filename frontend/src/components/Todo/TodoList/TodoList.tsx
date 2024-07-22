import {
  Card,
  CardBody,
  CardHeader,
  Heading,
  List,
  Text,
} from "@chakra-ui/react";
import { TodoItem } from "../TodoItem/TodoItem.tsx";
import { Todo } from "../types/TodoTypes.ts";

type TTodoList = {
  todos: Todo[];
  heading: string;
  deleteTodo: (value: number) => Promise<void>;
};

export const TodoList = ({ todos, heading, ...rest }: TTodoList) => {
  return (
    <Card width="100%">
      <CardHeader>
        <Heading size={"md"}>{heading}</Heading>
      </CardHeader>
      <CardBody>
        {todos.length ? (
          <List display={"flex"} flexDirection={"column"} gap={4}>
            {todos.map((todo, index) => (
              <TodoItem key={index} todo={todo} {...rest} />
            ))}
          </List>
        ) : (
          <Text>Нет задач</Text>
        )}
      </CardBody>
    </Card>
  );
};
