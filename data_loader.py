import torch
from torchvision import datasets, transforms


class Dataset:
    def __init__(self, dataset, _batch_size):
        super(Dataset, self).__init__()
        if dataset == 'mnist':
            dataset_transform = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,))
            ])

            train_dataset = datasets.MNIST('./data/mnist', train=True, download=True,
                                           transform=dataset_transform)
            test_dataset = datasets.MNIST('./data/mnist', train=False, download=True,
                                          transform=dataset_transform)

            self.train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=_batch_size, shuffle=True)
            self.test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=_batch_size, shuffle=False)

        elif dataset == 'cifar10':
            image_size = 24
            data_transform_train = transforms.Compose([
                transforms.ToTensor(),
                transforms.RandomCrop(size=(image_size, image_size)),
                transforms.RandomHorizontalFlip(),
                transforms.ColorJitter(brightness=0.2, contrast=(0.2, 1.8), saturation=0.2),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])
            data_transform_test = transforms.Compose([
                transforms.ToTensor(),
                transforms.RandomCrop(size=(image_size, image_size)),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])
            train_dataset = datasets.CIFAR10(
                './data/cifar', train=True, download=True, transform=data_transform_train)
            test_dataset = datasets.CIFAR10(
                './data/cifar', train=False, download=True, transform=data_transform_test)

            self.train_loader = torch.utils.data.DataLoader(
                train_dataset, batch_size=_batch_size, shuffle=True)

            self.test_loader = torch.utils.data.DataLoader(
                test_dataset, batch_size=_batch_size, shuffle=False)
        elif dataset == 'office-caltech':
            pass
        elif dataset == 'office31':
            pass
