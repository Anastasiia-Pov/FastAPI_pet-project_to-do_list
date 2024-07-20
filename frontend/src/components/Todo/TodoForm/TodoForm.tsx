import {
  Button,
  ButtonGroup,
  Card,
  CardBody,
  CardFooter,
  CardHeader,
  Input,
  Text,
  useToast,
} from "@chakra-ui/react";
import { TTodoForm } from "../types/TodoTypes.ts";
import { Controller, FormProvider, useForm } from "react-hook-form";
import { getDefaultValues } from "../helpers.ts";

type TTodoFormProps = {
  createTodo: (value: TTodoForm) => Promise<void>;
};

export const TodoForm = (props: TTodoFormProps) => {
  const toast = useToast();

  const { handleSubmit, reset, ...methods } = useForm<TTodoForm>({
    defaultValues: getDefaultValues(),
  });

  const onSubmit = async (data: TTodoForm) => {
    toast({ description: data.text });
    await props.createTodo(data);
    reset();
  };

  return (
    <FormProvider handleSubmit={handleSubmit} reset={reset} {...methods}>
      <Card width="100%" height={"100%"}>
        <CardHeader>
          <Text fontSize={"xl"} fontWeight={"bold"}>
            Создать новую задачу
          </Text>
        </CardHeader>
        <CardBody>
          <Controller
            render={({ field }) => (
              <Input
                name={"text"}
                value={field.value}
                onChange={field.onChange}
                placeholder={"Введите название новой задачи"}
                errorBorderColor={"red"}
              />
            )}
            name={"text"}
            rules={{ required: true }}
          />
          {methods.formState.errors.text ? (
            <Text color={"red"}>Введите текст</Text>
          ) : null}
        </CardBody>
        <CardFooter>
          <ButtonGroup>
            <Button colorScheme={"green"} onClick={handleSubmit(onSubmit)}>
              Сохранить
            </Button>
            <Button onClick={() => reset()}>Сбросить</Button>
          </ButtonGroup>
        </CardFooter>
      </Card>
    </FormProvider>
  );
};
