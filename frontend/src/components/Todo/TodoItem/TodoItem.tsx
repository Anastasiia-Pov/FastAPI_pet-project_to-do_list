import {
  Button,
  ButtonGroup,
  Card,
  Flex,
  Heading,
  ListItem,
  Progress,
  Text,
} from "@chakra-ui/react";
import { DeleteIcon, EditIcon } from "@chakra-ui/icons";
import { TaskPriorities, Todo } from "../types/TodoTypes.ts";

type TTodoItem = {
  todo: Todo;
  deleteTodo: (value: number) => Promise<void>;
};

export const TodoItem = (props: TTodoItem) => {
  const deleteTodo = async () => {
    await props.deleteTodo(props.todo.id);
  };

  const calculateProgress = (priority: TaskPriorities) => {
    switch (priority) {
      case TaskPriorities.Low:
        return {
          value: 33,
          colorScheme: "green",
        };
      case TaskPriorities.Medium:
        return {
          value: 66,
          colorScheme: "yellow",
        };
      case TaskPriorities.High:
        return {
          value: 100,
          colorScheme: "red",
        };
    }
  };

  return (
    <Card p={5}>
      <Flex flexDirection={"column"} gap={8}>
        <ListItem>
          <Heading size={"sm"}>{props.todo.task}</Heading>
          <Text>{props.todo.description}</Text>
          <Heading size={"xs"}>Приоритет</Heading>
          <Progress {...calculateProgress(props.todo.priority)} />
        </ListItem>
        <ButtonGroup>
          <Button
            isDisabled={true}
            colorScheme={"blue"}
            leftIcon={<EditIcon />}
            size={"sm"}
          >
            Редактировать
          </Button>
          <Button
            onClick={deleteTodo}
            colorScheme={"red"}
            leftIcon={<DeleteIcon />}
            size={"sm"}
          >
            Удалить
          </Button>
        </ButtonGroup>
      </Flex>
    </Card>
  );
};
