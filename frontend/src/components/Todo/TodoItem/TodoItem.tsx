import { Button, ButtonGroup, Flex, ListItem, Switch } from "@chakra-ui/react";
import { DeleteIcon, EditIcon } from "@chakra-ui/icons";
import { Todo } from "../types/TodoTypes.ts";

type TTodoItem = {
  todo: Todo;
  deleteTodo: (value: string) => Promise<void>;
  patchTodo: (value: string) => Promise<void>;
  toggleTodo: (value: string) => Promise<void>;
};

export const TodoItem = (props: TTodoItem) => {
  const toggleTodo = async () => {
    await props.toggleTodo(props.todo.text);
  };

  const patchTodo = async () => {
    await props.patchTodo(props.todo.text);
  };

  const deleteTodo = async () => {
    await props.deleteTodo(props.todo.text);
  };

  return (
    <Flex alignItems="center" gap={8}>
      <Switch
        colorScheme={"teal"}
        isChecked={props.todo.is_active}
        onChange={toggleTodo}
      />
      <ListItem minWidth={200}>{props.todo.text}</ListItem>
      <ButtonGroup>
        <Button
          isDisabled={true}
          onClick={patchTodo}
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
  );
};
