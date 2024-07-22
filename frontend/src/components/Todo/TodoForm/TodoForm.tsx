import {
  Button,
  ButtonGroup,
  Card,
  CardBody,
  CardFooter,
  CardHeader,
  Input,
  Modal,
  ModalContent,
  ModalOverlay,
  Select,
  Stack,
  Text,
  Textarea,
} from "@chakra-ui/react";
import { TaskPriorities, TaskStatuses, TTodoForm } from "../types/TodoTypes.ts";
import { Controller, FormProvider, useForm } from "react-hook-form";
import { getDefaultValues } from "../helpers.ts";
import { CloseIcon } from "@chakra-ui/icons";

type TTodoFormProps = {
  isVisible: boolean;
  closeForm: () => void;
  submitTodo: (value: TTodoForm) => Promise<void>;
};

export const TodoForm = ({
  isVisible,
  closeForm,
  submitTodo,
}: TTodoFormProps) => {
  const { handleSubmit, reset, ...methods } = useForm<TTodoForm>({
    defaultValues: getDefaultValues(),
  });

  const onSubmit = async (data: TTodoForm) => {
    await submitTodo(data);
    reset();
    closeForm();
  };

  return (
    <Modal isOpen={isVisible} onClose={closeForm}>
      <ModalOverlay />
      <ModalContent>
        <FormProvider handleSubmit={handleSubmit} reset={reset} {...methods}>
          <Card>
            <CardHeader display="flex" justifyContent="space-between">
              <Text fontSize={"xl"} fontWeight={"bold"}>
                Создать новую задачу
              </Text>
              <Button
                onClick={closeForm}
                colorScheme={"red"}
                size={"sm"}
                leftIcon={<CloseIcon marginInlineEnd={"0"} />}
              >
                Закрыть
              </Button>
            </CardHeader>
            <CardBody>
              <Stack spacing={"10px"}>
                <Controller
                  render={({ field }) => (
                    <Input
                      name={"task"}
                      value={field.value}
                      onChange={field.onChange}
                      placeholder={"Введите название новой задачи"}
                      errorBorderColor={"red"}
                      isInvalid={!!methods.formState.errors.task}
                    />
                  )}
                  name={"task"}
                  rules={{ required: true }}
                />
                {methods.formState.errors.task ? (
                  <Text color={"red"}>Введите текст</Text>
                ) : null}
                <Controller
                  render={({ field }) => (
                    <Textarea
                      maxHeight={"300px"}
                      name={"description"}
                      value={field.value}
                      onChange={field.onChange}
                      placeholder={"Введите описание новой задачи"}
                      errorBorderColor={"red"}
                      isInvalid={!!methods.formState.errors.description}
                    />
                  )}
                  name={"description"}
                  rules={{ required: true }}
                />
                {methods.formState.errors.description ? (
                  <Text color={"red"}>Введите описание</Text>
                ) : null}
                <Controller
                  render={({ field }) => (
                    <Select
                      name={"status"}
                      value={field.value}
                      onChange={field.onChange}
                      placeholder={"Выберите статус"}
                      errorBorderColor={"red"}
                    >
                      <option value={TaskStatuses.InProgress}>
                        В процессе
                      </option>
                      <option value={TaskStatuses.Waiting}>Ожидание</option>
                      <option value={TaskStatuses.Done}>Готово</option>
                    </Select>
                  )}
                  name={"status"}
                  rules={{ required: true }}
                />
                <Controller
                  render={({ field }) => (
                    <Select
                      defaultValue={"Low"}
                      name={"priority"}
                      value={field.value}
                      onChange={field.onChange}
                      placeholder={"Выберите приоритет"}
                      errorBorderColor={"red"}
                    >
                      <option value={TaskPriorities.Low}>Низкий</option>
                      <option value={TaskPriorities.Medium}>Средний</option>
                      <option value={TaskPriorities.High}>Высокий</option>
                    </Select>
                  )}
                  name={"priority"}
                  rules={{ required: true }}
                />
              </Stack>
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
      </ModalContent>
    </Modal>
  );
};
