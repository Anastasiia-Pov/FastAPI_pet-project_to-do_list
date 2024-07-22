export enum TaskPriorities {
  Low = "low",
  Medium = "medium",
  High = "high",
}

export enum TaskStatuses {
  Waiting = "waiting",
  InProgress = "in_progress",
  Done = "done",
}

export type Todo = {
  id: number;
  task: string;
  description: string;
  priority: TaskPriorities;
  status: TaskStatuses;
};

export type TTodoForm = {
  id?: number;
  task: string;
  description: string;
  priority: TaskPriorities;
  status: TaskStatuses;
};
