import { TaskPriorities, TaskStatuses, TTodoForm } from "./types/TodoTypes.ts";

export const getDefaultValues = (): TTodoForm => {
  return {
    task: "",
    description: "",
    priority: TaskPriorities.Low,
    status: TaskStatuses.Waiting,
  };
};
